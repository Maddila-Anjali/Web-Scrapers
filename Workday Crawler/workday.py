import os
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
OUTPUT_DIR = "workday_jobs_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paths to the JSON files
COMPANY_URLS_FILE = "company_urls.json"
SELECTORS_FILE = "css_selectors.json"

# Function to initialize the Selenium WebDriver
def init_driver():
    chrome_driver_path = "/opt/homebrew/bin/chromedriver"  # Update this path with your system path
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no browser UI)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Function to fetch jobs from a Workday careers page
def fetch_jobs(driver, company_name, careers_url, selectors):
    driver.get(careers_url)
    time.sleep(5)  # Wait for the page to load

    jobs = []
    page_number = 1

    try:
        while True:
            print(f"Fetching jobs from page {page_number} for {company_name}...")

            # Wait for job listings to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selectors["job_list"]))
            )

            # Extract job listings
            job_listings = driver.find_elements(By.CSS_SELECTOR, selectors["job_list"])

            for job in job_listings:
                try:
                    # Extract job title
                    job_title = job.find_element(By.CSS_SELECTOR, selectors["job_title"]).text.strip()

                    # Extract job location
                    job_location = job.find_element(By.CSS_SELECTOR, selectors["job_location"]).text.strip()

                    # Extract job link
                    job_link = job.find_element(By.CSS_SELECTOR, selectors["job_link"]).get_attribute("href")

                    # Append job details to the list
                    jobs.append({
                        "Job Title": job_title,
                        "Job Location": job_location,
                        "Job Link": job_link
                    })
                except Exception as e:
                    print(f"Error extracting job details for {company_name}: {e}")
                    continue

            # Check if there is a "Next" button and click it
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selectors["next_button"]))
                )
                next_button.click()
                time.sleep(5)  # Wait for the next page to load
                page_number += 1
            except Exception as e:
                #print(f"No more pages to crawl for {company_name} or error navigating to the next page: {e}")
                print(f"No more pages to crawl for {company_name}!!\n")
                break

    except Exception as e:
        print(f"Error fetching jobs for {company_name}: {e}")

    return jobs

# Function to save jobs to a CSV file
def save_to_csv(company_name, jobs):
    file_path = os.path.join(OUTPUT_DIR, f"{company_name}_jobs.csv")
    df = pd.DataFrame(jobs)
    df.to_csv(file_path, index=False, encoding="utf-8")
    print(f"Saved {len(jobs)} jobs to {file_path}.\n")

# Function to load JSON data from a file
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON data from {file_path}: {e}")
        return None

# Main function
def main():
    # Initialize the WebDriver
    driver = init_driver()

    try:
        # Load company URLs
        company_urls = load_json(COMPANY_URLS_FILE)
        if not company_urls:
            print("No company URLs found.")
            return

        # Load selectors
        selectors = load_json(SELECTORS_FILE)
        if not selectors:
            print("No selectors found.")
            return

        for company_name, careers_url in company_urls.items():
            print(f"Fetching jobs for {company_name}...")
            jobs = fetch_jobs(driver, company_name, careers_url, selectors)
            if jobs:
                save_to_csv(company_name, jobs)
            else:
                print(f"No jobs found for {company_name}.")
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()