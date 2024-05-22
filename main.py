import tkinter as tk
from tkinter import ttk, messagebox
from web_scraper import scrape_website
import logging
from threading import Thread
import time
import csv
import json

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def display_result(scraped_data):
    """
    Display the scraped data in a new window.
    """
    # Create a new window
    result_window = tk.Toplevel(root)
    result_window.title("Scraped Data")

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(result_window)
    scrollbar_x = ttk.Scrollbar(result_window, orient="horizontal", command=canvas.xview)
    scrollbar_y = ttk.Scrollbar(result_window, orient="vertical", command=canvas.yview)
    canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

    # Create a frame inside the canvas
    frame = ttk.Frame(canvas)
    frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Pack the canvas and scrollbars
    canvas.pack(side=tk.LEFT, fill='both', expand=True)
    scrollbar_x.pack(side=tk.BOTTOM, fill='x')
    scrollbar_y.pack(side=tk.RIGHT, fill='y')

    # Insert data into separate Text widgets in a grid layout
    for idx, data in enumerate(scraped_data):
        text_frame = ttk.Frame(frame)
        text_frame.grid(row=0, column=idx, padx=10, pady=10, sticky='nsew')
        
        text_widget = tk.Text(text_frame, wrap='word', padx=10, pady=10, state='normal', width=40, height=30)
        text_widget.pack(side=tk.LEFT, fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(text_frame, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        text_widget.config(yscrollcommand=scrollbar.set)

        if "error" in data:
            text_widget.insert(tk.END, f"Error scraping {data['url']}: {data['error']}\n\n")
        else:
            text_widget.insert(tk.END, f"Title of {data['url']}:\n\n{data['title']}\n\n")
            text_widget.insert(tk.END, f"Price: {data['price']}\n\n")
            text_widget.insert(tk.END, f"Description: {data['description']}\n\n")
            text_widget.insert(tk.END, f"Disclaimer:\n{data['disclaimer']}\n\n")
        
        text_widget.config(state='disabled')

def update_progress_message(status, total_time=None):
    """
    Update the progress label with the completion message.
    Update the time label with the total execution time.
    """
    progress_label.config(text=status)
    if total_time:
        time_label.config(text=f"Total execution time: {total_time:.2f} seconds")
    else:
        time_label.config(text="")

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

def save_to_json(scraped_data, filename='scraped_data.json'):
    """
    Save scraped data to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(scraped_data, output_file, ensure_ascii=False, indent=4)

    logging.info(f"Data saved to {filename}")

def scrape_and_display(urls):
    """
    Scrape the websites and display the results.
    """
    logging.info("Starting the web scraping process")
    progress_label.config(text="Scraping in progress...")

    def scrape_and_update():
        start_time = time.time()  # Înregistrare moment de început
        scraped_data = []

        # Update progress bar maximum
        progress_bar.config(maximum=len(urls))
        
        for i, url in enumerate(urls):
            data = scrape_website(url)
            scraped_data.append(data)
            
            # Update the progress bar
            progress_bar['value'] = i + 1
            root.update_idletasks()

        end_time = time.time()  # Înregistrare moment de sfârșit
        total_time = end_time - start_time  # Calcul timp total

        display_result(scraped_data)
        update_progress_message("Scraping completed", total_time)
        
        # Save scraped data to CSV and JSON files
        save_to_csv(scraped_data)
        save_to_json(scraped_data)

        logging.info("Completed the web scraping process")

    # Start scraping in a separate thread
    thread = Thread(target=scrape_and_update)
    thread.start()

def add_url_entry():
    """
    Add a new URL entry field.
    """
    if len(url_entries) >= 5:
        messagebox.showinfo("Maximum URLs reached", "You can add maximum 5 URLs.")
        return
    
    url_frame = ttk.Frame(urls_frame)
    url_frame.grid(row=len(url_entries), column=0, pady=5, sticky='ew')

    url_entry = ttk.Entry(url_frame, width=50)
    url_entry.pack(side=tk.LEFT, fill='x', expand=True)
    
    delete_button = ttk.Button(url_frame, text="-", command=lambda: remove_url_entry(url_frame))
    delete_button.pack(side=tk.RIGHT)

    url_entries.append(url_frame)

def remove_url_entry(url_frame):
    """
    Remove a URL entry field.
    """
    if len(url_entries) > 1:
        url_entries.remove(url_frame)
        url_frame.destroy()
    else:
        messagebox.showwarning("Minimum URLs", "There must be at least one URL entry.")

def validate_and_scrape():
    """
    Validate URL entries and start the scraping process if all are filled.
    """
    urls = [frame.winfo_children()[0].get() for frame in url_entries if frame.winfo_children()[0].get()]
    if len(urls) < len(url_entries):
        messagebox.showwarning("Incomplete URLs", "Please fill in all URL fields before scraping.")
        return
    scrape_and_display(urls)

def clear_results():
    """
    Clear all results displayed and reset all fields.
    """
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()
    for entry in url_entries:
        entry.winfo_children()[0].delete(0, tk.END)
    progress_label.config(text="")
    time_label.config(text="")
    progress_bar['value'] = 0

# Create the main window
root = tk.Tk()
root.title("Web Scraper")

# Style configuration
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#FF0000")
style.configure("TLabel", padding=6, background="#9B94FF")
style.configure("TFrame", background="#D8EFFF")

# Create a main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill='both', expand=True)

# Add a title label
title_label = ttk.Label(main_frame, text="Web Scraper", font=("Helvetica", 16))
title_label.grid(row=0, column=0, pady=10)

# Frame for URL entries
urls_frame = ttk.Frame(main_frame)
urls_frame.grid(row=1, column=0, pady=10)

# List to store URL entries
url_entries = []

# Add initial URL entry
add_url_entry()

# Buttons frame
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=2, column=0, pady=10)

# Button to add more URL entry fields
add_url_button = ttk.Button(buttons_frame, text="Add URL", command=add_url_entry)
add_url_button.grid(row=0, column=0, padx=5)

# Button to start scraping
scrape_button = ttk.Button(buttons_frame, text="Scrape Websites", command=validate_and_scrape)
scrape_button.grid(row=0, column=1, padx=5)

# Button to clear results
clear_button = ttk.Button(buttons_frame, text="Clear Results", command=clear_results)
clear_button.grid(row=0, column=2, padx=5)

# Progress label
progress_label = ttk.Label(main_frame, text="")
progress_label.grid(row=3, column=0, pady=10)

# Progress bar
progress_bar = ttk.Progressbar(main_frame, orient='horizontal', length=400, mode='determinate')
progress_bar.grid(row=4, column=0, pady=10)

# Time label
time_label = ttk.Label(main_frame, text="")
time_label.grid(row=5, column=0, pady=10)

# Configure grid weights
main_frame.columnconfigure(0, weight=1)
urls_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)
buttons_frame.columnconfigure(2, weight=1)

# Start the main loop
root.mainloop()
