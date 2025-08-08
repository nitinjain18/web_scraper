import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content from a news website
url = 'https://www.bbc.com/news'  # You can change to any other news site
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <h2> tags (commonly used for headlines)
    headline_tags = soup.find_all('h2')

    # Extract and clean the text content of each headline
    headlines = [tag.get_text(strip=True) for tag in headline_tags if tag.get_text(strip=True)]

    # Step 3: Save the headlines to a .txt file
    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for i, headline in enumerate(headlines, 1):
            file.write(f"{i}. {headline}\n")

    print("✅ Headlines successfully saved to 'headlines.txt'")

else:
    print(f"❌ Failed to retrieve the page. Status code: {response.status_code}")

