"""Extract soil-test values from digital PDFs and image files.

Supported inputs: PDF, PNG, JPG/JPEG, TIFF, BMP.
For image OCR and scanned PDFs, the Tesseract application must be installed
separately in addition to the Python package pytesseract.
"""

import re
from io import BytesIO

from PIL import Image, ImageOps
from pypdf import PdfReader

try:
    import pytesseract  # type: ignore
    HAS_PYTESSERACT = True
except ImportError:
    pytesseract = None
    HAS_PYTESSERACT = False


VALUE_KEYS = ("pH", "nitrogen", "phosphorus", "potassium")

# Use full nutrient names first; single-letter abbreviations are supported
# only when written as labels (e.g. "N: 280" or "P = 35").
LABELS = {
    "pH": r"p\s*h",
    "nitrogen": r"nitrogen|available\s+n|total\s+n|\bN\b",
    "phosphorus": r"phosphorus|phosphate|available\s+p|\bP\b",
    "potassium": r"potassium|potash|available\s+k|\bK\b",
}

NUMBER = r"([-+]?\d+(?:[.,]\d+)?)"
UNIT = r"(mg\s*/\s*kg|ppm|kg\s*/\s*ha|mg\s*/\s*ha|%|cmol\s*\(\s*\+\s*\)\s*/\s*kg)?"

def _normalise_number(raw):
    """Convert a number string to float, accepting decimal comma."""
    return float(raw.replace(",", "."))


def _read_image_ocr(image):
    """OCR an image with basic preprocessing."""
    if not HAS_PYTESSERACT or pytesseract is None:
        return (
            "IMAGE_OCR_UNAVAILABLE: Optical Character Recognition for images requires 'pytesseract'. "
            "Please enter your soil parameters manually below."
        )

    try:
        image = ImageOps.exif_transpose(image).convert("RGB")
        # Enlarge small scans to improve OCR results.
        if image.width < 1400:
            scale = 1400 / image.width
            image = image.resize((1400, int(image.height * scale)))
        return pytesseract.image_to_string(image, config="--psm 6")
    except Exception as exc:
        return f"OCR_PROCESSING_FAILED: Could not read image text ({exc}). Enter values manually."


def extract_text(uploaded_file):
    """Return extracted text from a Streamlit UploadedFile-like object."""
    filename = (getattr(uploaded_file, "name", "") or "").lower()
    content = uploaded_file.getvalue()

    if filename.endswith(".pdf"):
        reader = PdfReader(BytesIO(content))
        pages_text = []
        for page in reader.pages:
            pages_text.append(page.extract_text() or "")
        text = "\n".join(pages_text).strip()

        if text:
            return text

        # If the PDF has no selectable text, attempt OCR on its pages.
        try:
            import fitz  # type: ignore # PyMuPDF
        except ImportError:
            return (
                "SCANNED_PDF_NEEDS_OCR: This PDF appears to be scanned. "
                "Install PyMuPDF with 'python -m pip install pymupdf' and "
                "make sure Tesseract OCR is installed."
            )

        try:
            doc = fitz.open(stream=content, filetype="pdf")
            ocr_pages = []
            for page in doc:
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                image = Image.open(BytesIO(pix.tobytes("png")))
                ocr_pages.append(_read_image_ocr(image))
            doc.close()
            return "\n".join(ocr_pages).strip()
        except Exception as exc:
            return f"SCANNED_PDF_OCR_FAILED: Could not OCR scanned PDF ({exc})."

    if filename.endswith((".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp")):
        image = Image.open(BytesIO(content))
        return _read_image_ocr(image)

    return "UNSUPPORTED_FILE: Please upload a PDF, PNG, JPG, JPEG, TIFF or BMP file."


def _find_value(text, label_pattern):
    """Find a number close to a recognised label and optional unit."""
    # Label before value: "Nitrogen: 280 kg/ha", "pH 6.5"
    patterns = [
        # Label can appear at the start of a line or after words such as "Soil".
        rf"(?im)\b(?:{label_pattern})\b\s*[:=\-]?\s*{NUMBER}\s*{UNIT}",
        # Label and value may be separated by whitespace in a table.
        rf"(?i)\b(?:{label_pattern})\b\s+{NUMBER}\s*{UNIT}",
        # Value before label: "6.5 pH" or "280 kg/ha Nitrogen"
        rf"(?i){NUMBER}\s*{UNIT}\s*(?:{label_pattern})\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            # In all patterns, the first capturing group is the numeric value.
            try:
                value = _normalise_number(match.group(1))
            except (ValueError, AttributeError):
                continue
            unit = ""
            # The optional unit is not consistently in the same group index.
            for group in match.groups()[1:]:
                if group and re.search(r"[a-zA-Z%]", group):
                    unit = re.sub(r"\s+", "", group)
                    break
            return value, unit
    return None, ""


def extract_soil_values(text):
    """Return values and units found in extracted report text."""
    values = {}
    units = {}
    for key in VALUE_KEYS:
        value, unit = _find_value(text, LABELS[key])
        values[key] = value
        units[key] = unit
    return values, units


def read_soil_report(uploaded_file):
    """Return values, units, missing fields and source text, or an error."""
    try:
        text = extract_text(uploaded_file)

        if text.startswith("UNSUPPORTED_FILE:"):
            return {"error": text}
        if text.startswith("SCANNED_PDF_NEEDS_OCR:"):
            return {
                "error": text,
                "values": {key: None for key in VALUE_KEYS},
                "units": {key: "" for key in VALUE_KEYS},
                "missing": list(VALUE_KEYS),
            }
        if text.startswith("SCANNED_PDF_OCR_FAILED:"):
            return {
                "error": text,
                "values": {key: None for key in VALUE_KEYS},
                "units": {key: "" for key in VALUE_KEYS},
                "missing": list(VALUE_KEYS),
            }
        if not text.strip():
            return {
                "error": "No readable text was found in this file.",
                "values": {key: None for key in VALUE_KEYS},
                "units": {key: "" for key in VALUE_KEYS},
                "missing": list(VALUE_KEYS),
            }

        values, units = extract_soil_values(text)
        missing = [key for key, value in values.items() if value is None]
        return {
            "values": values,
            "units": units,
            "missing": missing,
            "extracted_text": text,
        }
    except Exception as exc:
        return {
            "error": (
                "Could not read this report. Try another file or enter the "
                f"values manually. Details: {exc}"
            ),
            "values": {key: None for key in VALUE_KEYS},
            "units": {key: "" for key in VALUE_KEYS},
            "missing": list(VALUE_KEYS),
        }
