# Business Leads Scraper

A Python scraper designed to collect professional business leads from websites efficiently and export them in a structured format.

## Features
- Collect company emails and contact information
- Configurable scraping options
- Export results to CSV or JSON
- Modular code structure for easy maintenance and extension

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