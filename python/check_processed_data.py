import sqlite3
import pandas as pd

def check_database(db_path):
    conn = sqlite3.connect(db_path)
    
    # Fetch the table names
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql_query(query, conn)
    
    print("Tables in the database:")
    print(tables)
    
    # For each table, fetch and print the first few rows
    for table in tables['name']:
        print(f"\nContents of table {table}:")
        query = f"SELECT * FROM {table} LIMIT 5;"
        table_data = pd.read_sql_query(query, conn)
        print(table_data)
        
        # Check the date column specifically
        if 'date' in table_data.columns:
            print(f"\nUnique dates in {table}:")
            unique_dates = pd.read_sql_query(f"SELECT DISTINCT date FROM {table}", conn)
            print(unique_dates)
    
    conn.close()

if __name__ == "__main__":
    db_path = '../data/processed_data.db'
    check_database(db_path)
