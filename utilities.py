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
        response.raise_for_status()
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
        products = []

        # Find all product elements
        product_elements = soup.find_all('div', class_='card-item card-standard js-product-data')

        for product in product_elements:
            title_element = product.find('a', class_='card-v2-title')
            price_element = product.find('p', class_='product-new-price')

            title = title_element.text.strip() if title_element else 'No title'
            price_text = price_element.text.strip() if price_element else 'No price found'

            # Convert price to float if possible
            price = ''.join(filter(str.isdigit, price_text.split()[0]))
            price = float(price) if price else 0.0

            products.append({
                "title": title,
                "price": price / 100
            })

        logging.info("Successfully parsed HTML content")
        return products
    except Exception as e:
        logging.error(f"Error parsing HTML content - {e}")
        return []

def scrape_website(url):
    """
    Scrape the given website URL and extract relevant data.
    """
    html_content = make_request(url)
    if html_content:
        data = parse_html(html_content)
        return data
    else:
        return []
