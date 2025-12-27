# Design Document – Days 01 to 07 (Hinglish Summary)

## Day 01 – System Health Check
- **Goal:** Monitor CPU usage using `psutil`.
- **Key Learnings:**
  - Import external libraries.
  - Use `try/except` for user input validation.
  - Wrap logic in functions (`get_cpu_threshold`, `check_cpu`).
  - Add `if __name__ == "__main__":` guard.
- **Result:** `improved_check_cpu.py` prints alert when CPU > threshold.

## Day 02 – Stock Market API
- **Goal:** Fetch stock data from Alpha Vantage.
- **Key Learnings:**
  - Use `requests` for HTTP calls.
  - Handle API keys (environment variable vs hard‑code).
  - Parse JSON and check for error messages.
  - Use `argparse` for CLI arguments (`symbol`, `--timeseries`).
- **Result:** `api_json_task.py` returns quote or daily time‑series.

## Day 03 – OpenWeatherMap Example
- **Goal:** Get current weather for a city.
- **Key Learnings:**
  - Read API key from env variable.
  - Build query parameters (`q`, `appid`, `units`).
  - Proper error handling for network & JSON decode.
  - Print concise JSON summary.
- **Result:** `openweather_app.py` works after setting a valid API key.

## Day 04 – Log Analyzer (Practice)
- **Goal:** Read a log file, count `INFO`, `WARNING`, `ERROR`.
- **Key Learnings:**
  - File I/O with `open` and `readlines`.
  - Use `collections.Counter` for counting.
  - CLI with `argparse` (`logfile`, `-o`, `-j`).
  - Write summary to terminal and optional output file.
- **Result:** `log_analyzer.py` in `day-04/practice` produces correct counts.

## Day 05 – Enhanced Log Analyzer
- **Goal:** Add `UNKNOWN` level handling and richer output.
- **Key Learnings:**
  - Extend counting to dynamic log levels.
  - Show summary in a formatted block.
  - Keep script reusable for different log files.
- **Result:** `sample_log_analyzer.py` shows counts for INFO, WARNING, ERROR, UNKNOWN.

## Day 06 – Configuration Management (YAML)
- **Goal:** Parse a YAML config file, validate keys, display summary.
- **Key Learnings:**
  - Install and use `PyYAML`.
  - Write modular functions: `load_yaml`, `validate_config`, `print_summary`.
  - Use `argparse` for `--file` argument.
  - Handle `FileNotFoundError`, `yaml.YAMLError`, and custom `ValueError`.
- **Result:** `config_parser.py` reads `config.yaml` and prints a clean summary.
- **Additional:** CLI version of log analyzer (`log_analyzer_cli.py`) with level filter.

## Day 07 – (Placeholder)
- **Goal:** Continue building DevOps tooling (e.g., Docker, CI/CD scripts).
- **Key Learnings (expected):**
  - Containerization basics.
  - Writing Dockerfiles.
  - Integrating scripts into CI pipelines.
  - Using environment variables securely.

---
**Overall Takeaway:** Across 7 days we covered:
1. System monitoring (`psutil`).
2. API consumption (`requests`).
3. Error handling & CLI design (`argparse`).
4. Log file processing (`Counter`).
5. Configuration parsing (`yaml`).
6. Building reusable, modular Python scripts for real‑world DevOps tasks.

Happy coding!
