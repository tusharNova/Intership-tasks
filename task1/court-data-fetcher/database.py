import sqlite3
import datetime
import json

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect('court_data.db')
    cursor = conn.cursor()
    
    # Create queries table to log all search attempts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT NOT NULL,
            case_number TEXT NOT NULL,
            filing_year INTEGER NOT NULL,
            query_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            raw_response TEXT,
            success BOOLEAN DEFAULT FALSE,
            error_message TEXT
        )
    ''')
    
    # Create case_data table to store successful case information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS case_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_id INTEGER,
            case_number_full TEXT,
            parties TEXT,
            filing_date TEXT,
            next_hearing TEXT,
            orders_json TEXT,
            status TEXT,
            FOREIGN KEY (query_id) REFERENCES queries (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def log_query(case_type, case_number, filing_year, response_data, success, error_message=None):
    """Log a query to the database"""
    conn = sqlite3.connect('court_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, raw_response, success, error_message)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, json.dumps(response_data), success, error_message))
    
    query_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return query_id

def save_case_data(query_id, case_data):
    """Save successfully parsed case data"""
    conn = sqlite3.connect('court_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO case_data (query_id, case_number_full, parties, filing_date, next_hearing, orders_json, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        query_id,
        case_data.get('case_number_full', ''),
        case_data.get('parties', ''),
        case_data.get('filing_date', ''),
        case_data.get('next_hearing', ''),
        json.dumps(case_data.get('orders', [])),
        case_data.get('status', '')
    ))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()