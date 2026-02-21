import requests
from bs4 import BeautifulSoup
import os

# Choose between local test file or real website
test_local = True

if test_local:
    path = os.path.join('data', 'sample_business_directory.html')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: file {path} not found.")
        exit()
else:
    url = 'https://example.com/business-directory'
    try:
        res = requests.get(url)
        res.raise_for_status()
        html_content = res.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        exit()

soup = BeautifulSoup(html_content, 'html.parser')

# User input for scraping choice
print('What do you want to scrape?')
print('(1) Websites')
print('(2) Emails')
print('(3) Phone numbers')

try:
    scrape_choice = int(input('> '))
except ValueError:
    print("Error: please enter an integer.")
    exit()

if scrape_choice == 1:
    elements = soup.select('.website')
elif scrape_choice == 2:
    elements = soup.select('.email')
elif scrape_choice == 3:
    elements = soup.select('.phone')
else:
    print("Error: choose a number between 1 and 3.")
    exit()

print(f"{len(elements)} elements found.")

# User input for exporting choice
print('In wich format do you want to export them ?')
print('(1) csv')
print('(2) json')
print('(3) just print them here')

try:
    export_choice = int(input('> '))
except ValueError:
    print("Error: please enter an integer.")
    exit()

if export_choice == 1:
    test = 1
elif export_choice == 2:
    test = 2
elif export_choice == 3:
    for elem in elements[:5]:
        print(elem.get_text(strip=True))
else:
    print("Error: choose a number between 1 and 3.")
    exit()