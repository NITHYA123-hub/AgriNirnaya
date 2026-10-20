
"""Weather service for AgriNirnay using Open-Meteo."""

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

DISTRICT_WEATHER_LOCATIONS = {
    "Bagalkot": "Bagalkot",
    "Ballari": "Bellary",
    "Belagavi": "Belgaum",
    "Bengaluru Rural": "Devanahalli",
    "Bengaluru Urban": "Bengaluru",
    "Bidar": "Bidar",
    "Chamarajanagar": "Chamarajanagar",
    "Chikkaballapur": "Chikkaballapur",
    "Chikkamagaluru": "Chikmagalur",
    "Chitradurga": "Chitradurga",
    "Dakshina Kannada": "Mangaluru",
    "Davanagere": "Davanagere",
    "Dharwad": "Dharwad",
    "Gadag": "Gadag",
    "Hassan": "Hassan",
    "Haveri": "Haveri",
    "Kalaburagi": "Gulbarga",
    "Kodagu": "Madikeri",
    "Kolar": "Kolar",
    "Koppal": "Koppal",
    "Mandya": "Mandya",
    "Mysuru": "Mysuru",
    "Raichur": "Raichur",
    "Ramanagara": "Ramanagara",
    "Shivamogga": "Shivamogga",
    "Tumakuru": "Tumakuru",
    "Udupi": "Udupi",
    "Uttara Kannada": "Karwar",
    "Vijayanagara": "Hosapete",
    "Vijayapura": "Vijayapura",
    "Yadgir": "Yadgir",
}


def get_weather(city: str) -> dict:
    """Return current weather and a three-day forecast."""

    city = (city or "").strip()

    if not city:
        return {"error": "Please select a farm location first."}

    search_location = DISTRICT_WEATHER_LOCATIONS.get(city, city)

    try:
        # Find the town's coordinates.
        geo_response = requests.get(
            GEOCODING_URL,
            params={
                "name": search_location,
                "count": 10,
                "language": "en",
                "format": "json",
            },
            timeout=15,
        )
        geo_response.raise_for_status()

        results = geo_response.json().get("results") or []

        # Fall back to the original location name if necessary.
        if not results and search_location != city:
            geo_response = requests.get(
                GEOCODING_URL,
                params={
                    "name": city,
                    "count": 10,
                    "language": "en",
                    "format": "json",
                },
                timeout=15,
            )
            geo_response.raise_for_status()
            results = geo_response.json().get("results") or []

        if not results:
            return {
                "error": (
                    f"No location found for '{city}'. "
                    "Try a nearby town or city."
                )
            }

        # Prefer Karnataka, India when available.
        place = next(
            (
                result
                for result in results
                if result.get("country_code") == "IN"
                and result.get("admin1", "").lower() == "karnataka"
            ),
            results[0],
        )

        latitude = place.get("latitude")
        longitude = place.get("longitude")

        if latitude is None or longitude is None:
            return {"error": "Location coordinates are unavailable."}

        # Request current conditions, hourly rain data and daily forecast.
        weather_response = requests.get(
            FORECAST_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "precipitation,"
                    "rain,"
                    "weather_code,"
                    "wind_speed_10m,"
                    "apparent_temperature"
                ),
                "hourly": (
                    "precipitation,"
                    "precipitation_probability"
                ),
                "daily": (
                    "temperature_2m_max,"
                    "temperature_2m_min,"
                    "precipitation_sum,"
                    "precipitation_probability_max"
                ),
                "forecast_days": 3,
                "timezone": "auto",
            },
            timeout=15,
        )
        weather_response.raise_for_status()

        data = weather_response.json()
        current = data.get("current")

        if not current:
            return {"error": "Current weather data is unavailable."}

        daily = data.get("daily") or {}
        hourly = data.get("hourly") or {}

        rainfall_values = daily.get("precipitation_sum") or [None]
        probability_values = (
            daily.get("precipitation_probability_max") or [None]
        )

        w_code = current.get("weather_code", 0)
        condition_map = {
            0: "☀️ Clear Sky",
            1: "🌤️ Mainly Clear",
            2: "⛅ Partly Cloudy",
            3: "☁️ Overcast",
            45: "🌫️ Foggy",
            48: "🌫️ Depositing Rime Fog",
            51: "🌦️ Light Drizzle",
            53: "🌦️ Moderate Drizzle",
            55: "🌧️ Dense Drizzle",
            61: "🌧️ Slight Rain",
            63: "🌧️ Moderate Rain",
            65: "🌧️ Heavy Rain",
            71: "🌨️ Slight Snow",
            80: "🌦️ Light Rain Showers",
            81: "🌧️ Moderate Showers",
            82: "⛈️ Violent Rain Showers",
            95: "⛈️ Thunderstorm",
            96: "⛈️ Thunderstorm with Hail",
        }
        condition_text = condition_map.get(w_code, "🌤️ Partly Cloudy")

        return {
            "city": place.get("name", search_location),
            "admin1": place.get("admin1", ""),
            "country": place.get("country", ""),
            "latitude": latitude,
            "longitude": longitude,
            "temperature": current.get("temperature_2m"),
            "apparent_temperature": current.get(
                "apparent_temperature"
            ),
            "humidity": current.get("relative_humidity_2m"),
            "precipitation": current.get("precipitation"),
            "rain": current.get("rain"),
            "weather_code": w_code,
            "condition": condition_text,
            "wind_speed": current.get("wind_speed_10m"),
            "time": current.get("time"),
            "daily": daily,
            "hourly": hourly,
            "today_rainfall_forecast": rainfall_values[0],
            "today_rain_probability": probability_values[0],
            "timezone": data.get("timezone", ""),
        }

    except requests.Timeout:
        return {
            "error": "Weather request timed out. Please try again."
        }

    except requests.RequestException:
        return {
            "error": (
                "Could not connect to the weather service. "
                "Check your internet connection and try again."
            )
        }

    except (ValueError, TypeError, IndexError):
        return {
            "error": "The weather service returned unreadable data."
        }
