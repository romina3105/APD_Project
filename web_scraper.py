from utilities import scrape_website
import concurrent.futures
import logging
import time

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_multiple_websites(urls):
    """
    Function to scrape multiple websites concurrently.
    """
    all_scraped_data = []
    
    start_time = time.time()

    # Concurrently scrape each website
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(scrape_website, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                all_scraped_data.extend(data)
            except Exception as e:
                logging.error(f"Error scraping {url}: {e}")
                continue
    
    logging.info("Completed scraping all websites")

    end_time = time.time()
    total_time = end_time - start_time 

    return all_scraped_data, total_time
