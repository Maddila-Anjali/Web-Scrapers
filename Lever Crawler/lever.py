import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch job listings from a Lever careers page
def crawl_lever_jobs(company_name, company_careers_url):
    try:
        # Send a GET request to the company's Lever careers page
        response = requests.get(company_careers_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page for {company_name}: {e}")
        return [], company_name  # Return company name for logging error

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the job listings (Lever uses <a> tags for job postings)
    job_listings = []
    job_elements = soup.find_all('a', class_='posting-title')  # Adjust this class name if needed

    for job_element in job_elements:
        # Extract job title, location, and link
        title = job_element.find('h5').text.strip() if job_element.find('h5') else "No Title"
        location = job_element.find('span', class_='sort-by-location').text.strip() if job_element.find('span', class_='sort-by-location') else "No Location"
        link = job_element['href']
        
        job_listings.append({
            'Company Name': company_name,
            'Job Title': title,
            'Location': location,
            'Job URL': link
        })

    return job_listings, None  # Return None for no error

# Function to read company names from the file and generate Lever URLs
def generate_lever_urls(file_name="lever_companies.txt"):
    companies = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                company_name = line.strip()  # Remove extra spaces or newlines
                if company_name:  # Skip empty lines
                    # Construct the Lever careers URL
                    company_url = f"https://jobs.lever.co/{company_name.lower()}"
                    companies.append((company_name, company_url))
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    return companies

# Function to save all job listings to a single CSV file
def save_jobs_to_csv(job_listings, filename="lever_jobs.csv"):
    if job_listings:
        df = pd.DataFrame(job_listings)
        df.to_csv(filename, index=False)
        print(f"Saved {len(job_listings)} job listings to {filename}")
    else:
        print("No job listings to save.")

# Function to log companies with errors
def log_error_companies(error_companies, filename="lever_companies_with_errors.txt"):
    with open(filename, 'w') as file:
        for company_name in error_companies:
            file.write(f"{company_name}\n")
    print(f"Logged {len(error_companies)} companies with errors to {filename}")

# Main function to process multiple companies
def main():
    file_name = "lever_companies.txt"  # File containing company names
    print(f"Reading company names from file: {file_name}")
    
    companies = generate_lever_urls(file_name)

    if not companies:
        print("No company names found. Please check the file format.")
        return

    all_job_listings = []
    error_companies = []  # List to track companies with errors
    for company_name, company_careers_url in companies:
        print(f"Fetching job listings for {company_name} from {company_careers_url}...")
        job_listings, error_company = crawl_lever_jobs(company_name, company_careers_url)
        if error_company:
            error_companies.append(error_company)
        else:
            all_job_listings.extend(job_listings)

    # Save valid job listings to a CSV file
    if all_job_listings:
        save_jobs_to_csv(all_job_listings)
    else:
        print("No job listings found for any company.")

    # Log companies with errors to a text file
    if error_companies:
        log_error_companies(error_companies)
    else:
        print("No errors encountered for any company.")

# Run the script
if __name__ == '__main__':
    main()
