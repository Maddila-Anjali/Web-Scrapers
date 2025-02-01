# Greenhouse Job Scraper

This project script scrapes job listings from Greenhouse career pages for a list of companies. It extracts job titles, locations, and URLs, and saves the data into a CSV file. Additionally, it logs companies that encounter errors during the scraping process.

## Features
- Automated Job Scraping: Fetches job listings from multiple companies using Greenhouse.
- Error Logging: Logs companies that encounter errors (e.g., redirects or inaccessible pages).
- Simple Configuration: Uses a text file to input company names.
- CSV Output: Saves job data into a single CSV file.

## Technologies Used
- Python
- BeautifulSoup
- Requests
- Pandas

## How to Run
1. Clone the repository:
   git clone https://github.com/your-username/Web-Crawlers.git

2. Install dependencies:
    pip install requests beautifulsoup4 pandas

3. Configuration:
   Company Names: Add the company names to a text file named greenhouse_companies.txt. Each company name should be on a new line.

4. Run the script:
    python greenhouse.py

## Output
- CSV File: The script generates a CSV file named greenhouse_jobs.csv containing the following columns:

Company Name: The name of the company.
Job Title: The title of the job.
Location: The location of the job.
Job URL: The URL to the job listing.

- Error Log: If any companies encounter errors, they are logged in greenhouse_companies_with_errors.txt.
