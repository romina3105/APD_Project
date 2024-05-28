import logging
import time
from utilities import scrape_website

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_multiple_websites_sequential(urls):
    """
    Function to scrape multiple websites sequentially.
    """
    all_scraped_data = []
    
    start_time = time.time()

    for url in urls:
        data = scrape_website(url)
        all_scraped_data.extend(data)
    
    logging.info("Completed scraping all websites")

    end_time = time.time()
    total_time = end_time - start_time 

    return all_scraped_data, total_time
