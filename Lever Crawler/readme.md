# Lever Job Scraper

This project script scrapes job listings from Lever career pages for a list of companies. It extracts job titles, locations, and URLs, and saves the data into a CSV file. Additionally, it logs companies that encounter errors during the scraping process.


## Features
- Reads the lever_companies.txt file which contains the names of the companies that use Lever to post their company jobs.
- Scrapes job listings from Lever-powered career pages.
- Saves extracted data in a structured format (CSV).
- Handles pagination to collect multiple job postings.

## Technologies Used
- Python
- BeautifulSoup
- Requests
- Pandas
- Selenium

## How to Run
1. Clone the repository:
   git clone https://github.com/your-username/Web-Crawlers.git

2. Install dependencies:
    pip install requests beautifulsoup4 pandas

3. Configuration:
   Company Names: Add the company names to a text file named lever_companies.txt. Each company name should be on a new line.

4. Run the script:
    python lever.py

## Output
- CSV File: The script generates a CSV file named lever.csv containing the following columns:

Company Name: The name of the company.
Job Title: The title of the job.
Location: The location of the job.
Job URL: The URL to the job listing.

- Error Log: If any companies encounter errors, they are logged in lever_companies_with_errors.txt.
