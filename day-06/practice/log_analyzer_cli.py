import argparse
import sys
from collections import Counter

def parse_log(file_path: str) -> Counter:
    """Parse the log file and count occurrences of each log level.

    Returns a Counter with keys like 'INFO', 'WARNING', 'ERROR', and any other
    levels that appear in the file.
    """
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
                # Capture any other word that looks like a level (e.g., DEBUG)
                # Simple heuristic: split and check for uppercase words
                for token in line.split():
                    if token.isupper() and token not in {"INFO", "WARNING", "ERROR"}:
                        counts[token] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    return counts

def filter_counts(counts: Counter, level: str | None) -> Counter:
    """If a specific level is requested, return a Counter with only that level.
    Otherwise return the original Counter.
    """
    if level is None:
        return counts
    filtered = Counter()
    if level.upper() in counts:
        filtered[level.upper()] = counts[level.upper()]
    else:
        print(f"Warning: Level '{level}' not found in log.", file=sys.stderr)
    return filtered

def write_summary(counts: Counter, out_path: str | None) -> None:
    """Print the summary to stdout and optionally write to a file."""
    for level, cnt in counts.items():
        print(f"{level}: {cnt}")
    if out_path:
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                for level, cnt in counts.items():
                    f.write(f"{level}: {cnt}\n")
        except OSError as e:
            print(f"Error writing summary: {e}", file=sys.stderr)

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI log analyzer for DevOps.")
    parser.add_argument("--file", required=True, help="Path to the log file (e.g., app.log)")
    parser.add_argument("--out", help="File to write the summary (optional)")
    parser.add_argument("--level", help="Filter to a single log level (e.g., ERROR)")
    args = parser.parse_args()

    counts = parse_log(args.file)
    counts = filter_counts(counts, args.level)
    write_summary(counts, args.out)

if __name__ == "__main__":
    main()
