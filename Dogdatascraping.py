import requests
from bs4 import BeautifulSoup

# Define the URL of the page to scrape
url = "https://pitbuliai.lt/apie-veisle/pitbulio-charakteris/"

# Step 1: Fetch the page content
response = requests.get(url)
if response.status_code == 200:
    # Step 2: Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Locate the main content text using a CSS selector or tag
    # Inspecting the page source, we can see that the article text is inside 'div' with class 'entry-content'
    content_div = soup.find('div', class_='entry-content')

    # Step 4: Extract and print the text
    if content_div:
        page_text = content_div.get_text(separator="\n").strip()
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(page_text)
        print(page_text)
    else:
        print("Content not found on the page.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
