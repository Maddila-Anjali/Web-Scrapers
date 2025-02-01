# Workday Job Scraper

This Project script uses Selenium to scrape job listings from Workday career pages. It extracts job titles, locations, and links, and saves the data into CSV files for each company.

## Features
- Automated Job Scraping: Fetches job listings from multiple companies.
- Headless Browser: Runs in headless mode for efficiency.
- Customizable Selectors: Uses JSON files to define CSS selectors for scraping.
- Input: Also reads the company_urls.json file to crawl a particular company workday.
- Pagination: Handles pagination to collect multiple job postings through its appropriate CSS Selector.
- CSV Output: Saves job data into separate CSV files for each company.

## Technologies Used
- Python
- Requests
- Pandas
- Selenium
- ChromeDriver
  
## How to Run
1. Clone the repository:
   git clone https://github.com/your-username/Web-Crawlers.git

2. Install dependencies:
    pip install selenium pandas

3. Download ChromeDriver:
   Ensure you have ChromeDriver installed and its path correctly set in the script.
   You can download ChromeDriver from the [ChromeDriver website](https://sites.google.com/chromium.org/driver/).

4. Configuration:
   Company URLs: Add the company names and their corresponding Workday career page URLs in company_urls.json file.

5. Run the script:
    python workday.py

The script will:

1. Initialize the WebDriver.
2. Load company URLs and CSS selectors from the JSON files.
3. Scrape job listings for each company.
4. Save the job data into CSV files in the workday_jobs_output directory.

## Output
The script generates CSV files named {company_name}_jobs.csv in the workday_jobs_output directory. Each file contains the following columns:

Job Title: The title of the job.
Job Location: The location of the job.
Job Link: The URL to the job listing.

## Troubleshooting
ChromeDriver Path: Ensure the chrome_driver_path variable in the script points to the correct location of your ChromeDriver.