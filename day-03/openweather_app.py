import argparse
import json
import os
import sys
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# OpenWeatherMap API key – set this environment variable before running.
API_KEY = "5d325dbbb80160dd27b0fc5c08f41bb4"
if not API_KEY:
    print(
        "Error: OPENWEATHER_API_KEY environment variable not set. "
        "Obtain a free API key from https://openweathermap.org/ and set it.",
        file=sys.stderr,
    )
    sys.exit(1)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str, units: str = "metric") -> dict:
    """Fetch current weather data for a city.

    Args:
        city: Name of the city (e.g., "London").
        units: "metric" for Celsius or "imperial" for Fahrenheit.
    Returns:
        Parsed JSON response from OpenWeatherMap.
    Raises:
        requests.RequestException: Network‑related errors.
        ValueError: If the API returns an error or the response cannot be decoded.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}", file=sys.stderr)
        raise
    try:
        data = response.json()
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON response: {e}", file=sys.stderr)
        raise ValueError("Invalid JSON response")
    # OpenWeatherMap uses a numeric "cod" field for errors.
    if data.get("cod") != 200:
        message = data.get("message", "Unknown error")
        raise ValueError(f"API error: {message}")
    return data


def display_summary(data: dict) -> None:
    """Print a concise weather summary.

    Shows temperature, weather description, humidity and wind speed.
    """
    main = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    wind = data.get("wind", {})
    summary = {
        "city": data.get("name"),
        "temperature": main.get("temp"),
        "description": weather.get("description"),
        "humidity": main.get("humidity"),
        "wind_speed": wind.get("speed"),
    }
    # Remove any ``None`` values for a cleaner output.
    summary = {k: v for k, v in summary.items() if v is not None}
    print(json.dumps(summary, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch current weather for a city using the OpenWeatherMap free API."
    )
    parser.add_argument("city", help="City name (e.g., London, New York)")
    parser.add_argument(
        "-u",
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="Units for temperature – 'metric' (Celsius) or 'imperial' (Fahrenheit).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        data = fetch_weather(args.city, args.units)
        display_summary(data)
    except Exception:
        # Errors are already printed inside helper functions.
        sys.exit(1)


if __name__ == "__main__":
    main()
