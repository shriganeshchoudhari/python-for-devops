import argparse
import sys
import yaml
from typing import Dict, Any

def load_yaml(file_path: str) -> Dict[str, Any]:
    """Load a YAML configuration file.

    Returns the parsed dictionary.
    Raises FileNotFoundError if the file does not exist.
    Raises yaml.YAMLError for malformed YAML.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.", file=sys.stderr)
        raise
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}", file=sys.stderr)
        raise

def validate_config(config: Dict[str, Any], required_keys: list) -> None:
    """Validate that required keys exist in the config.

    Raises ValueError if any required key is missing.
    """
    missing = [key for key in required_keys if key not in config]
    if missing:
        raise ValueError(f"Missing required configuration keys: {', '.join(missing)}")

def print_summary(config: Dict[str, Any]) -> None:
    """Print a concise summary of the configuration."""
    print("Configuration Summary:")
    for key, value in config.items():
        if isinstance(value, list):
            print(f"- {key}:")
            for item in value:
                print(f"  - {item}")
        else:
            print(f"- {key}: {value}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Load and validate a YAML config file.")
    parser.add_argument("--file", required=True, help="Path to the YAML configuration file")
    args = parser.parse_args()
    try:
        cfg = load_yaml(args.file)
        validate_config(cfg, ["environment", "version", "services"])
        print_summary(cfg)
    except Exception:
        # Errors already printed in helper functions.
        sys.exit(1)

if __name__ == "__main__":
    main()
