# Instructions :
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.
import requests
import time

def measure_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

sites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.amazon.co.il"]
for site in sites:
    load_time = measure_page_load_time(site)
    print(f"Page load time for {site}: {load_time} seconds")


