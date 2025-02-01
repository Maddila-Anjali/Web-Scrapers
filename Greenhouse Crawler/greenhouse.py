import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch job listings from a Greenhouse careers page
def crawl_greenhouse_jobs(company_name):
    greenhouse_url = f"https://boards.greenhouse.io/{company_name.lower()}"
    try:
        # Send a GET request to the Greenhouse URL
        response = requests.get(greenhouse_url, allow_redirects=True)  # Allow redirects

        # Check if the URL has been redirected
        if response.url != greenhouse_url:
            print(f"Redirect detected for {company_name}: {response.url}")
            return [], company_name  # Log the company name as an error due to redirect

        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {greenhouse_url} for {company_name}: {e}")
        return [], company_name  # Return company name for logging error

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = []
    job_elements = soup.find_all('div', class_='opening')

    for job_element in job_elements:
        title = job_element.find('a').text.strip() if job_element.find('a') else "No Title"
        location = job_element.find('span', class_='location').text.strip() if job_element.find('span', class_='location') else "No Location"
        link = job_element.find('a')['href'] if job_element.find('a') else None

        job_listings.append({
            'Company Name': company_name,
            'Job Title': title,
            'Location': location,
            'Job URL': f"https://boards.greenhouse.io{link}" if link else "No Link"
        })

    if not job_listings:
        print(f"No job postings found for {company_name}.")
        return [], company_name  # Log the company name as an error

    return job_listings, None  # Return None for no error

# Function to read company names from a file
def read_company_names(file_name="greenhouse_companies.txt"):
    companies = []
    try:
        with open(file_name, 'r') as file:
            companies = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    return companies

# Function to save job listings to a CSV file
def save_jobs_to_csv(job_listings, filename="greenhouse_jobs.csv"):
    if job_listings:
        df = pd.DataFrame(job_listings)
        df.to_csv(filename, index=False)
        print(f"Saved {len(job_listings)} job listings to {filename}")
    else:
        print("No job listings to save.")

# Function to log companies with errors
def log_error_companies(error_companies, filename="greenhouse_companies_with_errors.txt"):
    with open(filename, 'w') as file:
        for company_name in error_companies:
            file.write(f"{company_name}\n")
    print(f"Logged {len(error_companies)} companies with errors to {filename}")

# Main function
def main():
    file_name = "greenhouse_companies.txt"  # File containing company names
    print(f"Reading company names from file: {file_name}")
    
    companies = read_company_names(file_name)

    if not companies:
        print("No company names found. Please check the file.")
        return

    all_job_listings = []
    error_companies = []

    for company_name in companies:
        print(f"Fetching job listings for {company_name}...")
        
        # Crawl Greenhouse jobs
        job_listings, error_company = crawl_greenhouse_jobs(company_name)
        if error_company:
            error_companies.append(error_company)
        else:
            all_job_listings.extend(job_listings)

    # Save all job listings to a CSV file
    save_jobs_to_csv(all_job_listings)

    # Log companies with errors
    if error_companies:
        log_error_companies(error_companies)
    else:
        print("No errors encountered for any company.")

# Run the script
if __name__ == '__main__':
    main()