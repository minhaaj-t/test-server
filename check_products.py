import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
config = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT') or 3306),
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
    
    # Check if products table exists
    cursor.execute("SHOW TABLES LIKE 'products'")
    result = cursor.fetchone()
    
    if result:
        print("Products table exists")
        # Get table structure
        cursor.execute("DESCRIBE products")
        columns = cursor.fetchall()
        
        print("Structure of products table:")
        for column in columns:
            print(f"  - {column[0]}: {column[1]} ({'NULL' if column[2] == 'YES' else 'NOT NULL'})")
    else:
        print("Products table does not exist")
        
except Exception as e:
    print(f"Error: {e}")
    
finally:
    # Close connections
    if connection and connection.open:
        connection.close()