# Court Data Fetcher - Delhi High Court

A web application that fetches case information from Delhi High Court's public portal for educational and informational purposes.

## 🏛️ Court Chosen
**Delhi High Court** - https://delhihighcourt.nic.in/app/case-number

**Reason for Selection:**
- Stable website structure
- Clear form fields and data presentation
- Reliable public access
- Good data quality

## 🚀 Features

- Search cases by Case Type, Case Number, and Filing Year
- Handle CAPTCHA automatically
- Store search history in database
- Display case information in user-friendly format
- Responsive web design
- Error handling for invalid cases

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Chrome browser (for Selenium)
- Git

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd coubacrt-data-fetcher
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Setup environment variables**
```
cp .env.example .env
# Edit .env file with your configurations
```
5. **Initialize database**
```
python database.py
```
6. **Run the application**
```
python app.py
```
7. **Access the application Open http://localhost:5000 in your browser**


## 🔐 CAPTCHA Strategy
#### Current Implementation:
- Type: Simple text-based CAPTCHA
- Method: Automated extraction from HTML element (<span id="captcha-code">)
- Approach: Parse the displayed CAPTCHA number directly from the page source
- Reliability: High (text-based CAPTCHA is consistent)
#### Technical Details:

- CAPTCHA element: #captcha-code
- Hidden field: randomid (contains same value as displayed CAPTCHA)
- Refresh mechanism: Available but not needed for simple cases
- Audio support: Available for accessibility

#### Fallback Strategy:
If automated extraction fails, the system logs the error and provides clear feedback to the user.


## 📊 Sample Environment Variables

```env
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URL=sqlite:///court_data.db
DELHI_HC_BASE_URL=https://delhihighcourt.nic.in
SEARCH_TIMEOUT=30
CHROME_HEADLESS=True
```

## 🎯 Usage Examples

#### Successful Search

- Case Type: CS(OS)
- Case Number: 1
- Filing Year: 2024

#### Common Case Types

- S - CS(OS) - Civil Suit (Original Side)
- CW - W.P.(C) - Writ Petition (Civil)
- CRLA - CRL.A. - Criminal Appeal
- FAO - FAO - First Appeal from Order

## 🗃️ Database Schema
#### Queries Table

- id - Primary key
- case_type - Selected case type
- case_number - Entered case number
- filing_year - Selected year
- query_time - Timestamp of search
- raw_response - Full response data
- success - Boolean success flag
- error_message - Error details if failed

#### Case Data Table

- id - Primary key
- query_id - Foreign key to queries
- case_number_full - Complete case number
- parties - Parties involved
- filing_date - Date of filing/judgment
- next_hearing - Next hearing date
- orders_json - JSON array of orders
- status - Case status

## 🔧 Technical Stack

- Backend: Python Flask
- Database: SQLite
- Web Scraping: Selenium + BeautifulSoup
- Frontend: Bootstrap 5, HTML5, CSS3, JavaScript
- Browser Automation: Chrome WebDriver

## 🛡️ Legal Compliance
This project scrapes publicly available case information from Delhi High Court for educational/informational purposes only, in accordance with the court's stated policy that content is provided "for information purpose."

*Disclaimer* : This tool provides case information for reference only. Not for official legal use.

## 🐛 Error Handling

- Invalid case numbers
- Network timeouts
- CAPTCHA extraction failures
- Database connection issues
- Website structure changes