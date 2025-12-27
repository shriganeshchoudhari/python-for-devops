import argparse
import json
import sys
from collections import Counter

def parse_log(file_path: str) -> Counter:
    """Read the log file and count log levels."""
    counts = Counter()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line_lower = line.lower()
                if "info" in line_lower:
                    counts["INFO"] += 1
                if "warning" in line_lower:
                    counts["WARNING"] += 1
                if "error" in line_lower:
                    counts["ERROR"] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    return counts

def write_summary(counts: Counter, out_path: str, as_json: bool = False) -> None:
    """Write the summary to terminal and optionally to a JSON file."""
    summary = dict(counts)
    print("Log summary:")
    for level, cnt in summary.items():
        print(f"{level}: {cnt}")
    if out_path:
        try:
            if as_json:
                with open(out_path, "w", encoding="utf-8") as f:
                    json.dump(summary, f, indent=2)
            else:
                with open(out_path, "w", encoding="utf-8") as f:
                    for level, cnt in summary.items():
                        f.write(f"{level}: {cnt}\n")
        except OSError as e:
            print(f"Error writing summary: {e}", file=sys.stderr)

def main() -> None:
    parser = argparse.ArgumentParser(description="Simple log analyzer.")
    parser.add_argument("logfile", help="Path to the log file (e.g., app.log)")
    parser.add_argument("-o", "--output", help="File to write the summary")
    parser.add_argument("-j", "--json", action="store_true", help="Write summary as JSON")
    args = parser.parse_args()
    counts = parse_log(args.logfile)
    write_summary(counts, args.output, args.json)

if __name__ == "__main__":
    main()
