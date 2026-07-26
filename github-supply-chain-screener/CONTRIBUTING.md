# Contributing

Contributions should improve evidence quality, reduce false positives, or add safe detection coverage.

1. Do not submit live malware, credential material, or active exploit payloads.
2. Add an inert test fixture for every new scanner rule.
3. Explain the legitimate use case and expected false-positive trade-off.
4. Keep rules evidence-oriented: a match is a review signal, never an automatic malware verdict.
5. Run `python -m unittest discover -s tests` and the skill validator before opening a pull request.

Use a security report instead of an issue for vulnerabilities in this project.
