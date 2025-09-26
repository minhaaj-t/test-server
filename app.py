from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='frontend', static_url_path='')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model that matches the existing books table structure
class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    isbn = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(255), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)
    availability = db.Column(db.Enum('available', 'checked-out'), nullable=False)
    category = db.Column(db.Enum('fiction', 'non-fiction', 'academic', 'science', 'technology', 
                                'history', 'biography', 'children', 'reference', 'other'), nullable=False)
    publisher = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(8, 2), nullable=True)
    total_copies = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    department = db.Column(db.String(255), nullable=True)
    book_overview = db.Column(db.Text, nullable=True)
    page_images = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<Book {self.name}>'

# Define a model for products table
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False, default=0)
    image_url = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'

# Insert dummy data without dropping existing tables
def insert_dummy_data():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Check if we already have book data to avoid duplicates
        if Book.query.first() is None:
            # Insert dummy book data that matches the table structure
            books = [
                Book(
                    name='To Kill a Mockingbird',
                    author='Harper Lee',
                    isbn='978-0-06-112008-4',
                    language='English',
                    published_year=1960,
                    availability='available',
                    category='fiction',
                    publisher='J.B. Lippincott & Co.',
                    description='A gripping tale of racial injustice and childhood innocence.',
                    total_copies=5,
                    available_copies=3
                ),
                Book(
                    name='1984',
                    author='George Orwell',
                    isbn='978-0-452-28423-4',
                    language='English',
                    published_year=1949,
                    availability='available',
                    category='fiction',
                    publisher='Secker & Warburg',
                    description='A dystopian social science fiction novel and cautionary tale.',
                    total_copies=4,
                    available_copies=2
                ),
                Book(
                    name='Pride and Prejudice',
                    author='Jane Austen',
                    isbn='978-0-14-143951-8',
                    language='English',
                    published_year=1813,
                    availability='checked-out',
                    category='fiction',
                    publisher='T. Egerton',
                    description='A romantic novel of manners set in Georgian society.',
                    total_copies=3,
                    available_copies=0
                )
            ]
            
            for book in books:
                db.session.add(book)
            
            db.session.commit()
            print("Dummy book data inserted successfully!")
        else:
            print("Book data already exists, skipping insertion.")
            
        # Check if we already have product data to avoid duplicates
        if Product.query.first() is None:
            # Insert dummy product data
            products = [
                Product(
                    name='Wireless Headphones',
                    description='High-quality wireless headphones with noise cancellation',
                    price=129.99,
                    category='Electronics',
                    stock_quantity=25,
                    image_url='https://example.com/images/headphones.jpg'
                ),
                Product(
                    name='Coffee Maker',
                    description='Automatic drip coffee maker with programmable timer',
                    price=89.95,
                    category='Home Appliances',
                    stock_quantity=15,
                    image_url='https://example.com/images/coffee-maker.jpg'
                ),
                Product(
                    name='Fitness Tracker',
                    description='Water-resistant fitness tracker with heart rate monitor',
                    price=79.99,
                    category='Wearables',
                    stock_quantity=30,
                    image_url='https://example.com/images/fitness-tracker.jpg'
                ),
                Product(
                    name='Bluetooth Speaker',
                    description='Portable Bluetooth speaker with 10-hour battery life',
                    price=59.99,
                    category='Electronics',
                    stock_quantity=20,
                    image_url='https://example.com/images/speaker.jpg'
                ),
                Product(
                    name='Desk Lamp',
                    description='LED desk lamp with adjustable brightness and color temperature',
                    price=39.99,
                    category='Home & Office',
                    stock_quantity=40,
                    image_url='https://example.com/images/desk-lamp.jpg'
                )
            ]
            
            for product in products:
                db.session.add(product)
            
            db.session.commit()
            print("Dummy product data inserted successfully!")
        else:
            print("Product data already exists, skipping insertion.")

# Serve the frontend
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    # Check if the file exists in the static folder
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        # If the file doesn't exist, return the index.html for SPA routing
        if '.' not in path:  # If it's not a file with extension, treat as route
            return send_from_directory(app.static_folder, 'index.html')
        else:
            # For files with extensions, return 404 if not found
            return "File not found", 404

# API endpoint to get all books
@app.route('/api/books')
def get_books():
    books = Book.query.all()
    books_list = []
    for book in books:
        books_list.append({
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'isbn': book.isbn,
            'published_year': book.published_year,
            'availability': book.availability,
            'category': book.category
        })
    return {'books': books_list}

# API endpoint to get all products
@app.route('/api/products')
def get_products():
    products = Product.query.all()
    products_list = []
    for product in products:
        products_list.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price) if product.price else None,
            'category': product.category,
            'stock_quantity': product.stock_quantity,
            'image_url': product.image_url
        })
    return {'products': products_list}

if __name__ == '__main__':
    insert_dummy_data()
    # Use the PORT environment variable provided by Render, default to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)