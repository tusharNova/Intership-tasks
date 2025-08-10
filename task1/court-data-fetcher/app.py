from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import sqlite3
import json
from database import init_db, log_query, save_case_data
from scraper import DelhiHighCourtScraper
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# Initialize database on startup
init_db()

@app.route('/')
def index():
    """Home page with search form"""
    scraper = DelhiHighCourtScraper()
    case_types = scraper.get_case_types()
    
    # Generate year options (1951-2025)
    years = list(range(2025, 1950, -1))
    
    return render_template('index.html', case_types=case_types, years=years)

@app.route('/search', methods=['POST'])
def search_case():
    """Handle case search requests"""
    try:
        # Get form data
        case_type = request.form.get('case_type', '').strip()
        case_number = request.form.get('case_number', '').strip()
        filing_year = request.form.get('filing_year', '').strip()
        
        # Validate input
        if not all([case_type, case_number, filing_year]):
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))
        
        # Validate year
        try:
            filing_year = int(filing_year)
            if filing_year < 1951 or filing_year > 2025:
                flash('Invalid year. Please select a year between 1951 and 2025.', 'error')
                return redirect(url_for('index'))
        except ValueError:
            flash('Invalid year format.', 'error')
            return redirect(url_for('index'))
        
        # Initialize scraper
        scraper = DelhiHighCourtScraper()
        
        # Perform search
        flash(f'Searching for case: {case_type} {case_number}/{filing_year}...', 'info')
        case_data, success = scraper.get_case_data(case_type, case_number, filing_year)
        
        # Log the query
        error_message = case_data.get('error') if not success else None
        query_id = log_query(case_type, case_number, filing_year, case_data, success, error_message)
        
        if success and case_data.get('cases'):
            # Save case data
            save_case_data(query_id, {
                'case_number_full': f"{case_type} {case_number}/{filing_year}",
                'parties': case_data['cases'][0].get('parties', ''),
                'filing_date': case_data['cases'][0].get('date_of_judgment', ''),
                'next_hearing': '',
                'orders': case_data.get('cases', []),
                'status': 'Found'
            })
            
            flash('Case found successfully!', 'success')
            return render_template('results.html', 
                                 case_data=case_data,
                                 search_params={
                                     'case_type': case_type,
                                     'case_number': case_number,
                                     'filing_year': filing_year
                                 })
        else:
            error_msg = case_data.get('error', 'Case not found or no data available')
            flash(f'Search failed: {error_msg}', 'error')
            return render_template('results.html', 
                                 error=error_msg,
                                 search_params={
                                     'case_type': case_type,
                                     'case_number': case_number,
                                     'filing_year': filing_year
                                 })
    
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/history')
def search_history():
    """Display search history"""
    try:
        conn = sqlite3.connect('court_data.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT q.*, c.parties, c.status 
            FROM queries q 
            LEFT JOIN case_data c ON q.id = c.query_id 
            ORDER BY q.query_time DESC 
            LIMIT 50
        ''')
        
        history = cursor.fetchall()
        conn.close()
        
        return render_template('history.html', history=history)
    
    except Exception as e:
        flash(f'Error loading history: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/api/case-types')
def api_case_types():
    """API endpoint to get case types"""
    scraper = DelhiHighCourtScraper()
    return jsonify(scraper.get_case_types())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)