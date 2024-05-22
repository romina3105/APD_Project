import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def make_request(url):
    """
    Make an HTTP request to the given URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        logging.info(f"Successfully fetched URL: {url}")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Request failed for URL: {url} - {e}")
        return None

def parse_html(html_content):
    """
    Parse the HTML content using BeautifulSoup and extract relevant data.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        
        # Extract price and description if available
        price = soup.find('p', class_='product-new-price')
        description = soup.find('div', id='specifications-body')
        disclaimer = soup.find('div', class_='disclaimer-section')
        
        price_text = price.text.strip() if price else 'No price found'
        description_text = description.text.strip() if description else 'No description found'
        disclaimer_text = disclaimer.text.strip() if disclaimer else 'No disclaimer found'

        logging.info("Successfully parsed HTML content")
        return {
            "title": title,
            "price": price_text,
            "description": description_text,
            "disclaimer": disclaimer_text
        }
    except Exception as e:
        logging.error(f"Error parsing HTML content - {e}")
        return None

def scrape_website(url):
    """
    Scrape the given website URL and extract relevant data.
    """
    html_content = make_request(url)
    if html_content:
        data = parse_html(html_content)
        if data:
            data['url'] = url  # Add the URL to the returned data
        return data
    else:
        return {"url": url, "error": "Failed to retrieve content"}
