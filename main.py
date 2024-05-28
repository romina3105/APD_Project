import logging
import time
import csv
import matplotlib.pyplot as plt
from web_scraper import scrape_multiple_websites
from utilities import make_request
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_total_pages(category_url):
    """
    Get the total number of pages for a category.
    """
    html_content = make_request(category_url)
    if not html_content:
        return 0

    soup = BeautifulSoup(html_content, 'html.parser')
    pagination = soup.find('div', class_='pagination-container')
    if not pagination:
        return 1

    pages = pagination.find_all('a')
    total_pages = int(pages[-2].text) if pages else 1
    return total_pages

def generate_category_urls(base_url, total_pages):
    """
    Generate URLs for all pages in the category.
    """
    return [f"{base_url}/p{page}/c" for page in range(1, total_pages + 1)]

def save_to_csv(scraped_data, filename='scraped_data.csv'):
    """
    Save scraped data to a CSV file.
    """
    keys = scraped_data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(scraped_data)

    logging.info(f"Data saved to {filename}")


def generate_bar_chart(scraped_data, filename='chart10.png'):
    """
    Generate a bar chart of the top 10 most expensive products.
    """
    top_10_products = sorted(scraped_data, key=lambda x: x['price'], reverse=True)[:10]
    product_names = [product['title'] for product in top_10_products]
    product_prices = [product['price'] for product in top_10_products]

    plt.figure(figsize=(12, 8))
    plt.barh(product_names, product_prices, color='skyblue')
    plt.xlabel('Price')
    plt.title('Top 10 Most Expensive Products')
    plt.gca().invert_yaxis()
    plt.savefig(filename)
    plt.close()

    logging.info(f"Bar chart saved to {filename}")

def scrape_and_save(base_url):
    """
    Scrape the websites and save the results.
    """
    logging.info("Starting the web scraping process")

    total_pages = get_total_pages(base_url)
    urls = generate_category_urls(base_url, total_pages)
    
    scraped_data, total_time = scrape_multiple_websites(urls)

    # Save scraped data to CSV file
    save_to_csv(scraped_data)

    # Generate bar chart for top 10 most expensive products
    generate_bar_chart(scraped_data)

    # Calculate statistics
    total_products = len(scraped_data)
    prices = [product['price'] for product in scraped_data if product['price'] > 0]
    avg_price = sum(prices) / len(prices) if prices else 0
    min_price = min(prices) if prices else 0
    max_price = max(prices) if prices else 0

    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Number of products extracted: {total_products}")
    print(f"Average price: {avg_price :.2f}")
    print(f"Minimum price: {min_price :.2f}")
    print(f"Maximum price: {max_price :.2f}")

    logging.info("Completed the web scraping process")

if __name__ == "__main__":
    base_url = "https://www.emag.ro/telefoane-mobile"
    scrape_and_save(base_url)
