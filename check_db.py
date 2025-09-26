import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
config = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT') or 3306),  # Default to 3306 if not set
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

connection = None

try:
    # Create connection
    connection = pymysql.connect(**config)
    
    # Create cursor
    cursor = connection.cursor()
    
    # Get all tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    
    print("Tables in the database:")
    for table in tables:
        print(f"- {table[0]}")
        
        # Get table structure for books and products tables
        if table[0] in ['books', 'products']:
            cursor.execute(f"DESCRIBE {table[0]}")
            columns = cursor.fetchall()
            
            print(f"  Structure of {table[0]}:")
            for column in columns:
                print(f"    - {column[0]}: {column[1]} ({'NULL' if column[2] == 'YES' else 'NOT NULL'})")
            print()
        
except Exception as e:
    print(f"Error: {e}")
    
finally:
    # Close connections
    if connection and connection.open:
        connection.close()