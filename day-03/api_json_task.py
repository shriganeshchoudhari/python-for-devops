import argparse
import json
import os
import sys
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Direct API key assignment (provided by the user). In production, prefer an env var.
API_KEY = "QRHE86JT0WVBQLHI"
if not API_KEY:
    print(
        "Error: ALPHAVANTAGE_API_KEY not set. Please set the API key.",
        file=sys.stderr,
    )
    sys.exit(1)

BASE_URL = "https://www.alphavantage.co/query"

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def validate_symbol(symbol: str) -> str:
    """Validate that the provided stock symbol looks plausible.

    Args:
        symbol: The ticker symbol supplied by the user.
    Returns:
        Upper‑cased symbol if valid.
    Raises:
        ValueError: If the symbol is empty or contains non‑alphanumeric characters.
    """
    if not symbol:
        raise ValueError("Symbol cannot be empty.")
    if not symbol.isalnum():
        raise ValueError(
            f"Invalid symbol '{symbol}'. Symbols should contain only letters and numbers."
        )
    return symbol.upper()


def fetch_stock_data(symbol: str, timeseries: bool) -> dict:
    """Fetch stock market data from Alpha Vantage.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL").
        timeseries: If True, request daily time‑series data; otherwise, request a simple quote.
    Returns:
        Parsed JSON response.
    Raises:
        requests.RequestException: Network‑related errors.
        ValueError: If Alpha Vantage returns an error message.
    """
    params = {
        "apikey": API_KEY,
        "symbol": symbol,
        "function": "TIME_SERIES_DAILY" if timeseries else "GLOBAL_QUOTE",
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}", file=sys.stderr)
        raise
    data = response.json()
    if "Error Message" in data:
        raise ValueError(data["Error Message"])
    return data


def display_summary(data: dict, timeseries: bool) -> None:
    """Print a concise JSON summary of the fetched stock data.

    For a simple quote it shows price, volume and latest trading day.
    For a time series it shows the most recent day's OHLCV values.
    """
    if timeseries:
        series = data.get("Time Series (Daily)")
        if not series:
            print("No time‑series data available.", file=sys.stderr)
            return
        latest_date = sorted(series.keys(), reverse=True)[0]
        day_data = series[latest_date]
        summary = {
            "symbol": data.get("Meta Data", {}).get("2. Symbol", "N/A"),
            "date": latest_date,
            "open": day_data.get("1. open"),
            "high": day_data.get("2. high"),
            "low": day_data.get("3. low"),
            "close": day_data.get("4. close"),
            "volume": day_data.get("5. volume"),
        }
    else:
        quote = data.get("Global Quote", {})
        summary = {
            "symbol": quote.get("01. symbol"),
            "price": quote.get("05. price"),
            "volume": quote.get("06. volume"),
            "latest_trading_day": quote.get("07. latest trading day"),
        }
    # Remove any None values for cleaner output.
    summary = {k: v for k, v in summary.items() if v is not None}
    print(json.dumps(summary, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch stock market data from Alpha Vantage."
    )
    parser.add_argument("symbol", nargs="?", default="AAPL", help="Stock ticker symbol (default: AAPL)")
    parser.add_argument(
        "-t",
        "--timeseries",
        action="store_true",
        help="Retrieve daily time‑series data instead of a simple quote",
    )
    args = parser.parse_args()
    try:
        args.symbol = validate_symbol(args.symbol)
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        sys.exit(1)
    return args


def main() -> None:
    args = parse_args()
    try:
        data = fetch_stock_data(args.symbol, args.timeseries)
        display_summary(data, args.timeseries)
    except Exception:
        # Errors already printed in helper functions.
        sys.exit(1)

if __name__ == "__main__":
    main()

import json
import os
import sys
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Direct API key assignment (provided by the user). In production, prefer an env var.
API_KEY = "QRHE86JT0WVBQLHI"
if not API_KEY:
    print(
        "Error: ALPHAVANTAGE_API_KEY not set. Please set the API key.",
        file=sys.stderr,
    )
    sys.exit(1)

BASE_URL = "https://www.alphavantage.co/query"

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def validate_symbol(symbol: str) -> str:
    """Validate that the provided stock symbol looks plausible.

    Args:
        symbol: The ticker symbol supplied by the user.
    Returns:
        Upper‑cased symbol if valid.
    Raises:
        ValueError: If the symbol is empty or contains non‑alphanumeric characters.
    """
    if not symbol:
        raise ValueError("Symbol cannot be empty.")
    if not symbol.isalnum():
        raise ValueError(
            f"Invalid symbol '{symbol}'. Symbols should contain only letters and numbers."
        )
    return symbol.upper()


def fetch_stock_data(symbol: str, timeseries: bool) -> dict:
    """Fetch stock market data from Alpha Vantage.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL").
        timeseries: If True, request daily time‑series data; otherwise, request a simple quote.
    Returns:
        Parsed JSON response.
    Raises:
        requests.RequestException: Network‑related errors.
        ValueError: If Alpha Vantage returns an error message.
    """
    params = {
        "apikey": API_KEY,
        "symbol": symbol,
        "function": "TIME_SERIES_DAILY" if timeseries else "GLOBAL_QUOTE",
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}", file=sys.stderr)
        raise
    data = response.json()
    if "Error Message" in data:
        raise ValueError(data["Error Message"])
    return data


def display_summary(data: dict, timeseries: bool) -> None:
    """Print a concise JSON summary of the fetched stock data.

    For a simple quote it shows price, volume and latest trading day.
    For a time series it shows the most recent day's OHLCV values.
    """
    if timeseries:
        series = data.get("Time Series (Daily)")
        if not series:
            print("No time‑series data available.", file=sys.stderr)
            return
        latest_date = sorted(series.keys(), reverse=True)[0]
        day_data = series[latest_date]
        summary = {
            "symbol": data.get("Meta Data", {}).get("2. Symbol", "N/A"),
            "date": latest_date,
            "open": day_data.get("1. open"),
            "high": day_data.get("2. high"),
            "low": day_data.get("3. low"),
            "close": day_data.get("4. close"),
            "volume": day_data.get("5. volume"),
        }
    else:
        quote = data.get("Global Quote", {})
        summary = {
            "symbol": quote.get("01. symbol"),
            "price": quote.get("05. price"),
            "volume": quote.get("06. volume"),
            "latest_trading_day": quote.get("07. latest trading day"),
        }
    # Remove any None values for cleaner output.
    summary = {k: v for k, v in summary.items() if v is not None}
    print(json.dumps(summary, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch stock market data from Alpha Vantage."
    )
    parser.add_argument("symbol", nargs="?", default="AAPL", help="Stock ticker symbol (default: AAPL)")
    parser.add_argument(
        "-t",
        "--timeseries",
        action="store_true",
        help="Retrieve daily time‑series data instead of a simple quote",
    )
    args = parser.parse_args()
    try:
        args.symbol = validate_symbol(args.symbol)
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        sys.exit(1)
    return args


def main() -> None:
    args = parse_args()
    try:
        data = fetch_stock_data(args.symbol, args.timeseries)
        display_summary(data, args.timeseries)
    except Exception:
        # Errors already printed in helper functions.
        sys.exit(1)

if __name__ == "__main__":
    main()

import json
import os
import sys
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Direct API key assignment (provided by the user). In production, prefer an env var.
API_KEY = "QRHE86JT0WVBQLHI"
if not API_KEY:
    print(
        "Error: ALPHAVANTAGE_API_KEY environment variable not set. "
        "Please set it before running the script.",
        file=sys.stderr,
    )
    sys.exit(1)

BASE_URL = "https://www.alphavantage.co/query"

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def validate_symbol(symbol: str) -> str:
    """Validate that the provided stock symbol looks plausible.

    Args:
        symbol: The ticker symbol supplied by the user.
    Returns:
        Upper‑cased symbol if valid.
    Raises:
        ValueError: If the symbol is empty or contains non‑alphanumeric characters.
    """
    if not symbol:
        raise ValueError("Symbol cannot be empty.")
    if not symbol.isalnum():
        raise ValueError(
            f"Invalid symbol '{symbol}'. Symbols should contain only letters and numbers."
        )
    return symbol.upper()


def fetch_stock_data(symbol: str, timeseries: bool) -> dict:
    """Fetch stock market data from Alpha Vantage.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL").
        timeseries: If True, request daily time‑series data; otherwise, request a simple quote.
    Returns:
        Parsed JSON response.
    Raises:
        requests.RequestException: For network‑related errors.
        ValueError: If Alpha Vantage returns an error message.
    """
    params = {
        "apikey": API_KEY,
        "symbol": symbol,
        "function": "TIME_SERIES_DAILY" if timeseries else "GLOBAL_QUOTE",
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}", file=sys.stderr)
        raise

    data = response.json()
    if "Error Message" in data:
        raise ValueError(data["Error Message"])  # API‑level error
    return data


def display_summary(data: dict, timeseries: bool) -> None:
    """Print a concise JSON summary of the fetched stock data.

    For a simple quote it shows price, volume and latest trading day.
    For a time series it shows the most recent day's OHLCV values.
    """
    if timeseries:
        series = data.get("Time Series (Daily)")
        if not series:
            print("No time‑series data available.", file=sys.stderr)
            return
        latest_date = sorted(series.keys(), reverse=True)[0]
        day_data = series[latest_date]
        summary = {
            "symbol": data.get("Meta Data", {}).get("2. Symbol", "N/A"),
            "date": latest_date,
            "open": day_data.get("1. open"),
            "high": day_data.get("2. high"),
            "low": day_data.get("3. low"),
            "close": day_data.get("4. close"),
            "volume": day_data.get("5. volume"),
        }
    else:
        quote = data.get("Global Quote", {})
        summary = {
            "symbol": quote.get("01. symbol"),
            "price": quote.get("05. price"),
            "volume": quote.get("06. volume"),
            "latest_trading_day": quote.get("07. latest trading day"),
        }
    # Remove any None values for cleaner output.
    summary = {k: v for k, v in summary.items() if v is not None}
    print(json.dumps(summary, indent=2))


def parse_args() -> argparse.Namespace:
    """Parse command‑line arguments.

    Returns:
        Namespace with `symbol` (default "AAPL") and `timeseries` flag.
    """
    parser = argparse.ArgumentParser(
        description="Fetch stock market data from Alpha Vantage."
    )
    parser.add_argument(
        "symbol",
        nargs="?",
        default="AAPL",
        help="Stock ticker symbol (default: AAPL)",
    )
    parser.add_argument(
        "-t",
        "--timeseries",
        action="store_true",
        help="Retrieve daily time‑series data instead of a simple quote",
    )
    args = parser.parse_args()
    try:
        args.symbol = validate_symbol(args.symbol)
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        sys.exit(1)
    return args


def main() -> None:
    args = parse_args()
    try:
        data = fetch_stock_data(args.symbol, args.timeseries)
        display_summary(data, args.timeseries)
    except Exception:
        # Detailed errors already printed in helper functions.
        sys.exit(1)


if __name__ == "__main__":
    main()

import json
import os
import sys
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# The Alpha Vantage API key should be provided via an environment variable.
# This avoids hard‑coding secrets in source code.
API_KEY = os.getenv("QRHE86JT0WVBQLHI")
if not API_KEY:
    print(
        "Error: ALPHAVANTAGE_API_KEY environment variable not set. "
        "Please set it before running the script.",
        file=sys.stderr,
    )
    sys.exit(1)

BASE_URL = "https://www.alphavantage.co/query"

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def validate_symbol(symbol: str) -> str:
    """Validate that the provided stock symbol looks plausible.

    Args:
        symbol: The ticker symbol supplied by the user.
    Returns:
        The same symbol if it passes validation.
    Raises:
        ValueError: If the symbol is empty or contains non‑alphanumeric characters.
    """
    if not symbol:
        raise ValueError("Symbol cannot be empty.")
    if not symbol.isalnum():
        raise ValueError(
            f"Invalid symbol '{symbol}'. Symbols should contain only letters and numbers."
        )
    return symbol.upper()


def fetch_stock_data(symbol: str, timeseries: bool) -> dict:
    """Fetch stock market data from Alpha Vantage.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL").
        timeseries: If True, request daily time‑series data; otherwise, request a simple quote.
    Returns:
        Parsed JSON response from Alpha Vantage.
    Raises:
        requests.HTTPError: For HTTP‑related errors.
        ValueError: If the API returns an error message or unexpected format.
    """
    params = {
        "apikey": API_KEY,
        "symbol": symbol,
    }
    params["function"] = "TIME_SERIES_DAILY" if timeseries else "GLOBAL_QUOTE"
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}", file=sys.stderr)
        raise

    data = response.json()
    # Alpha Vantage signals errors with an "Error Message" key.
    if "Error Message" in data:
        raise ValueError(data["Error Message"])
    return data


def display_summary(data: dict, timeseries: bool) -> None:
    """Print a concise JSON summary of the fetched stock data.

    For a simple quote it shows price, volume and latest trading day.
    For a time series it shows the most recent day's OHLCV values.
    """
    if timeseries:
        series = data.get("Time Series (Daily)")
        if not series:
            print("No time‑series data available.", file=sys.stderr)
            return
        latest_date = sorted(series.keys(), reverse=True)[0]
        day_data = series[latest_date]
        summary = {
            "symbol": data.get("Meta Data", {}).get("2. Symbol", "N/A"),
            "date": latest_date,
            "open": day_data.get("1. open"),
            "high": day_data.get("2. high"),
            "low": day_data.get("3. low"),
            "close": day_data.get("4. close"),
            "volume": day_data.get("5. volume"),
        }
    else:
        quote = data.get("Global Quote", {})
        summary = {
            "symbol": quote.get("01. symbol"),
            "price": quote.get("05. price"),
            "volume": quote.get("06. volume"),
            "latest_trading_day": quote.get("07. latest trading day"),
        }
    # Remove any keys with None values for a cleaner output.
    summary = {k: v for k, v in summary.items() if v is not None}
    print(json.dumps(summary, indent=2))


def parse_args() -> argparse.Namespace:
    """Parse and validate command‑line arguments.

    Returns:
        An argparse.Namespace with the validated symbol and the timeseries flag.
    """
    parser = argparse.ArgumentParser(
        description="Fetch stock market data from Alpha Vantage."
    )
    parser.add_argument("symbol", help="Stock ticker symbol, e.g., AAPL, MSFT")
    parser.add_argument(
        "-t",
        "--timeseries",
        action="store_true",
        help="Retrieve daily time‑series data instead of a simple quote",
    )
    args = parser.parse_args()
    # Validate the symbol early so we can give a friendly error.
    try:
        args.symbol = validate_symbol(args.symbol)
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        sys.exit(1)
    return args


def main() -> None:
    args = parse_args()
    try:
        data = fetch_stock_data(args.symbol, args.timeseries)
        display_summary(data, args.timeseries)
    except Exception:
        # All detailed error messages are printed inside helper functions.
        sys.exit(1)


if __name__ == "__main__":
    main()

import json
import os
import sys
import requests

# Retrieve the Alpha Vantage API key from an environment variable for security.
API_KEY = "QRHE86JT0WVBQLHI"
if not API_KEY:
    print("Error: ALPHAVANTAGE_API_KEY environment variable not set.", file=sys.stderr)
    sys.exit(1)

BASE_URL = "https://www.alphavantage.co/query"


def fetch_stock_data(symbol: str, timeseries: bool) -> dict:
    """Fetch stock market data for a given symbol.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL").
        timeseries: If True, request daily time series data; otherwise, request a simple quote.
    Returns:
        Parsed JSON response from Alpha Vantage.
    Raises:
        requests.HTTPError: For HTTP‑related errors.
        ValueError: If the API returns an error message or unexpected format.
    """
    params = {
        "apikey": API_KEY,
        "symbol": symbol,
    }
    if timeseries:
        params["function"] = "TIME_SERIES_DAILY"
    else:
        params["function"] = "GLOBAL_QUOTE"
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}", file=sys.stderr)
        raise

    data = response.json()
    # Alpha Vantage returns an "Error Message" key on failure.
    if "Error Message" in data:
        raise ValueError(data["Error Message"])
    return data


def display_summary(data: dict, timeseries: bool) -> None:
    """Print a concise summary of the fetched stock data.

    For a simple quote, prints the price and volume.
    For a time series, prints the most recent day's open, high, low, close.
    """
    if timeseries:
        # The daily series is under the "Time Series (Daily)" key.
        series = data.get("Time Series (Daily)")
        if not series:
            print("No time series data available.", file=sys.stderr)
            return
        # Get the latest date (sorted descending).
        latest_date = sorted(series.keys(), reverse=True)[0]
        day_data = series[latest_date]
        summary = {
            "symbol": data.get("Meta Data", {}).get("2. Symbol", "N/A"),
            "date": latest_date,
            "open": day_data.get("1. open"),
            "high": day_data.get("2. high"),
            "low": day_data.get("3. low"),
            "close": day_data.get("4. close"),
            "volume": day_data.get("5. volume"),
        }
    else:
        quote = data.get("Global Quote", {})
        summary = {
            "symbol": quote.get("01. symbol"),
            "price": quote.get("05. price"),
            "volume": quote.get("06. volume"),
            "latest_trading_day": quote.get("07. latest trading day"),
        }
    # Remove None values for cleaner output.
    summary = {k: v for k, v in summary.items() if v is not None}
    print(json.dumps(summary, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch stock market data from Alpha Vantage.")
    parser.add_argument("symbol", help="Stock ticker symbol, e.g., AAPL, MSFT")
    parser.add_argument(
        "-t",
        "--timeseries",
        action="store_true",
        help="Retrieve daily time‑series data instead of a simple quote",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        data = fetch_stock_data(args.symbol, args.timeseries)
        display_summary(data, args.timeseries)
    except Exception as e:
        # Errors already printed inside helper functions.
        sys.exit(1)


if __name__ == "__main__":
    main()

import json
import sys
import requests


def fetch_json(url: str) -> dict:
    """Fetch JSON data from the given URL.

    Args:
        url: The API endpoint to request.
    Returns:
        Parsed JSON as a Python dictionary.
    Raises:
        requests.HTTPError: If the HTTP request returned an unsuccessful status code.
        ValueError: If the response content is not valid JSON.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}", file=sys.stderr)
        raise

    try:
        return response.json()
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON response from {url}: {e}", file=sys.stderr)
        raise ValueError("Invalid JSON response")


def display_summary(data: dict) -> None:
    """Print a concise summary of selected fields from the JSON data.

    This function extracts common repository information if the data follows the GitHub API
    schema, but works generically for any JSON object.
    """
    summary = {
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "stargazers_count": data.get("stargazers_count"),
        "forks_count": data.get("forks_count"),
    }
    # Remove keys with None values to keep output tidy
    summary = {k: v for k, v in summary.items() if v is not None}
    print(json.dumps(summary, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and display JSON from a given API endpoint.")
    parser.add_argument(
        "url",
        help="The API URL to fetch JSON from. Example: https://api.github.com/repos/python/cpython",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        data = fetch_json(args.url)
        display_summary(data)
    except Exception as e:
        # Errors have already been printed; exit with non‑zero status
        sys.exit(1)


if __name__ == "__main__":
    main()

import json


def fetch_json(url: str) -> dict:
    """Fetch JSON data from the given URL.

    Args:
        url: The API endpoint to request.
    Returns:
        Parsed JSON as a Python dictionary.
    Raises:
        requests.HTTPError: If the HTTP request returned an unsuccessful status code.
        ValueError: If the response content is not valid JSON.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        raise

    try:
        data = response.json()
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON response: {e}")
        raise ValueError("Invalid JSON response")
    return data


def main():
    # Example API – replace with the endpoint you need.
    api_url = "https://api.github.com/repos/python/cpython"
    try:
        result = fetch_json(api_url)
        # Pretty‑print a subset of the data
        print(json.dumps({
            "full_name": result.get("full_name"),
            "description": result.get("description"),
            "stargazers_count": result.get("stargazers_count"),
            "forks_count": result.get("forks_count"),
        }, indent=2))
    except Exception:
        # Errors are already printed in fetch_json
        pass


if __name__ == "__main__":
    main()
