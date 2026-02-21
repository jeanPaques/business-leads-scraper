import requests
from bs4 import BeautifulSoup
import os
import csv
import json

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
    label = 'website'
elif scrape_choice == 2:
    elements = soup.select('.email')
    label = 'email'
elif scrape_choice == 3:
    elements = soup.select('.phone')
    label = 'phone'
else:
    print("Error: choose a number between 1 and 3.")
    exit()

print(f"{len(elements)} elements found.")

# Normalize extracted data
data = []
for elem in elements:
    if scrape_choice == 1:
        value = elem.get('href')
    else:
        value = elem.get_text(strip=True)

    if value:
        data.append(value)

# User input for exporting choice
print('In which format do you want to export them?')
print('(1) CSV')
print('(2) JSON')
print('(3) Just print them here')

try:
    export_choice = int(input('> '))
except ValueError:
    print("Error: please enter an integer.")
    exit()

if export_choice == 1:
    os.makedirs('output', exist_ok=True)
    filename = os.path.join('output', f'{label}s.csv')

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([label])
        for item in data:
            writer.writerow([item])

    print(f"Exported to {filename}")

elif export_choice == 2:
    os.makedirs('output', exist_ok=True)
    filename = os.path.join('output', f'{label}s.json')

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Exported to {filename}")

elif export_choice == 3:
    for item in data:
        print(item)

else:
    print("Error: choose a number between 1 and 3.")
    exit()