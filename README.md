# Business Leads Scraper

A Python web scraping project to extract business contact data
(emails, websites, phone numbers) from HTML pages and export them to CSV or JSON.
Safe, modular, and easy-to-read code suitable for learning and portfolio demonstration.

## Features

- Extract emails, websites, or phone numbers from HTML pages
- Works with a local test HTML file for safe scraping practice
- Export results to CSV or JSON
- Simple and readable codebase with functions for modularity
- Designed for easy extension and learning Python web scraping concepts

## Installation

```bash
git clone https://github.com/jeanPaques/business-leads-scraper.git
cd business-leads-scraper
python -m venv venv
# On Windows use: venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py
```
## Local Test Data

This project includes a local HTML file used for development and testing.

- `data/sample_business_directory.html`
- Purpose: simulate a real business directory website
- Used to test scraping logic without hitting real websites
- Safe for offline development and unit testing

The structure is intentionally simple and consistent to focus on parsing logic.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT License