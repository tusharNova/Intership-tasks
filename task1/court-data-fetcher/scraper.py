import requests
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DelhiHighCourtScraper:
    def __init__(self):
        self.base_url = "https://delhihighcourt.nic.in"
        self.search_url = "https://delhihighcourt.nic.in/app/case-number"
        self.session = requests.Session()
        
    def setup_driver(self):
        """Setup Chrome driver with appropriate options"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def get_case_data(self, case_type, case_number, filing_year):
        """
        Main method to scrape case data from Delhi High Court
        """
        driver = None
        try:
            print(f"Starting search for: {case_type} {case_number}/{filing_year}")
            
            # Setup selenium driver
            driver = self.setup_driver()
            
            # Navigate to the search page
            driver.get(self.search_url)
            time.sleep(3)  # Wait for page to load
            
            # Extract CSRF token and captcha
            token = self.extract_token(driver)
            captcha_code = self.extract_captcha(driver)
            
            if not token or not captcha_code:
                return {"error": "Could not extract token or captcha"}, False
            
            # Fill the form
            success = self.fill_search_form(driver, case_type, case_number, filing_year, captcha_code)
            
            if not success:
                return {"error": "Failed to fill search form"}, False
            
            # Submit form and wait for results
            submit_button = driver.find_element(By.ID, "search")
            submit_button.click()
            
            # Wait for results to load
            time.sleep(5)
            
            # Parse results
            case_data = self.parse_results(driver)
            
            if case_data:
                return case_data, True
            else:
                return {"error": "No case data found or case doesn't exist"}, False
                
        except Exception as e:
            print(f"Error in scraping: {str(e)}")
            return {"error": str(e)}, False
            
        finally:
            if driver:
                driver.quit()

    def extract_token(self, driver):
        """Extract CSRF token from the page"""
        try:
            token_element = driver.find_element(By.NAME, "_token")
            return token_element.get_attribute("value")
        except Exception as e:
            print(f"Error extracting token: {e}")
            return None

    def extract_captcha(self, driver):
        """Extract captcha code from the page"""
        try:
            captcha_element = driver.find_element(By.ID, "captcha-code")
            captcha_code = captcha_element.text.strip()
            print(f"Extracted captcha: {captcha_code}")
            return captcha_code
        except Exception as e:
            print(f"Error extracting captcha: {e}")
            return None

    def fill_search_form(self, driver, case_type, case_number, filing_year, captcha_code):
        """Fill the search form with provided data"""
        try:
            # Select case type
            case_type_select = Select(driver.find_element(By.NAME, "case_type"))
            case_type_select.select_by_value(case_type)
            
            # Enter case number
            case_number_input = driver.find_element(By.NAME, "case_number")
            case_number_input.clear()
            case_number_input.send_keys(str(case_number))
            
            # Select year
            year_select = Select(driver.find_element(By.NAME, "year"))
            year_select.select_by_value(str(filing_year))
            
            # Enter captcha
            captcha_input = driver.find_element(By.NAME, "captchaInput")
            captcha_input.clear()
            captcha_input.send_keys(captcha_code)
            
            time.sleep(1)  # Small delay
            return True
            
        except Exception as e:
            print(f"Error filling form: {e}")
            return False

    def parse_results(self, driver):
        """Parse the results page and extract case information"""
        try:
            # Wait for results table to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "table"))
            )
            
            # Check if there's a "No data available" message
            page_source = driver.page_source
            if "No data available in table" in page_source:
                return None
            
            # Parse the results table
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # Find the results table
            table = soup.find('table')
            if not table:
                return None
            
            # Extract case information
            rows = table.find_all('tr')[1:]  # Skip header row
            
            if not rows:
                return None
            
            cases = []
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 4:
                    case_info = {
                        'serial_no': cells[0].get_text(strip=True),
                        'case_number_full': cells[1].get_text(strip=True),
                        'date_of_judgment': cells[2].get_text(strip=True),
                        'parties': cells[3].get_text(strip=True),
                        'corrigendum': cells[4].get_text(strip=True) if len(cells) > 4 else ''
                    }
                    cases.append(case_info)
            
            # Return the parsed data
            return {
                'cases': cases,
                'total_cases': len(cases),
                'search_successful': True
            }
            
        except Exception as e:
            print(f"Error parsing results: {e}")
            return None

    def get_case_types(self):
        """Get all available case types from the form"""
        case_types = [
            {"value": "S", "text": "CS(OS)"},
            {"value": "CW", "text": "W.P.(C)"},
            {"value": "CRLA", "text": "CRL.A."},
            {"value": "FAO", "text": "FAO"},
            {"value": "RFA", "text": "RFA"},
            {"value": "LPA", "text": "LPA"},
            {"value": "CAA", "text": "CA"},
            {"value": "MAT", "text": "MAT."},
            {"value": "CRLMA", "text": "CRL.M.A."},
            {"value": "CMA", "text": "CM APPL."}
        ]
        return case_types

# Test the scraper
if __name__ == "__main__":
    scraper = DelhiHighCourtScraper()
    
    # Test with a sample case
    result, success = scraper.get_case_data("S", "10", "2023")
    
    if success:
        print("Scraping successful!")
        print(json.dumps(result, indent=2))
    else:
        print("Scraping failed:")
        print(result)