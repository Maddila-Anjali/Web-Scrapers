# Web Scrapers

This repository contains three web scrapers designed to fetch job listings from different career platforms: Greenhouse, Lever, and Workday. Each scraper is implemented in Python and uses libraries such as Requests, BeautifulSoup, Selenium, and Pandas to extract and save job data.

## Features
- Greenhouse Scraper: Fetches job listings from Greenhouse career pages.
- Lever Scraper: Fetches job listings from Lever career pages.
- Workday Scraper: Fetches job listings from Workday career pages.
- CSV Output: Saves job data into CSV files for each platform.
- Error Logging: Logs companies that encounter errors during scraping.

## Technologies Used
- Python 3.x
- Requests
- BeautifulSoup
- Selenium
- Pandas
- ChromeDriver
  
## How to Run
1. Clone the repository:
   git clone https://github.com/your-username/Web-Crawlers.git

2. Install dependencies:
    pip install requests beautifulsoup4 selenium pandas

3. Download ChromeDriver:
   Ensure you have ChromeDriver installed and its path correctly set in the script.
   You can download ChromeDriver from the [ChromeDriver website](https://sites.google.com/chromium.org/driver/).

4. Run the script:
   a. Greenhouse Scraper : python greenhouse.py
   b. Lever Scraper : python lever.py
   c. Workday Scraper : python workday.py

Each script will:
1. Read company names or URLs from the respective configuration files.
2. Scrape job listings from the corresponding career pages.
3. Save the job data into CSV files in the respective output directories.
4. Log any companies that encountered errors during scraping.

## Output
The script generates CSV files named {company_name}_jobs.csv. Each file contains the following columns:

Job Title: The title of the job.
Job Location: The location of the job.
Job Link: The URL to the job listing.

## Troubleshooting
1. CSS Selectors: If the job listings are not being scraped correctly, update the CSS selectors in css_selectors.json.
2. ChromeDriver Path: Ensure the chrome_driver_path variable in the script points to the correct location of your ChromeDriver.