# Day 06 – Configuration Management & YAML Parsing

## Task

In this exercise you will practice **reading and handling configuration files** commonly used in DevOps pipelines. You will:

- Create a small YAML configuration file.
- Write a Python script that loads the YAML, validates required keys, and prints a concise summary.
- Add basic error handling for missing files, malformed YAML, and missing configuration values.
- Optionally expose the configuration via command‑line arguments.

## Expected Output

Running the script should display the loaded configuration in a readable format, for example:

```
Configuration Summary:
- environment: production
- version: 1.2.3
- services:
  - web
  - db
  - cache
```

## Guidelines

- Use the `yaml` module (`PyYAML`). Install it with `pip install pyyaml`.
- Keep the script modular: a function to load the file, a function to validate keys, and a `main()` entry point.
- Add `try/except` blocks to catch:
  - `FileNotFoundError` when the YAML file does not exist.
  - `yaml.YAMLError` for malformed content.
  - Custom `ValueError` for missing required keys.
- Follow PEP‑8 style and include type hints.

## Resources

- PyYAML documentation: https://pyyaml.org/wiki/PyYAMLDocumentation
- YAML basics: https://yaml.org/spec/1.2/spec.html
- Python `argparse` tutorial: https://docs.python.org/3/library/argparse.html

## Why This Matters for DevOps

Configuration files are the backbone of infrastructure‑as‑code, CI/CD pipelines, and container orchestration. Being able to reliably parse and validate them programmatically reduces deployment errors and improves automation.

## Submission

1. Add the `practice` folder inside `day-06`.
2. Place the `config_parser.py` script and a sample `config.yaml` file there.
3. Run the script to ensure it prints the expected summary.
4. Commit and push your changes.

---

Happy Learning!
[TrainWithShubham](https://www.trainwithshham.com/)
