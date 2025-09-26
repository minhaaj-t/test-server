# Flask MySQL Server

A Python Flask application that connects to a MySQL database and provides API endpoints for a library management system with a frontend interface.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up your database credentials in the `.env` file:
   ```
   DB_HOST=db.fr-pari1.bengt.wasmernet.com
   DB_PORT=10272
   DB_NAME=library_management
   DB_USER=7e4ca751759c8000463db46b28a7
   DB_PASSWORD=068b7e4c-a751-77af-8000-cb2911e1c700
   ```

## Running the Server Locally

Start the Flask server:
```
python app.py
```

The server will be available at `http://localhost:5000`

## Deploying to Render.com

See [RENDER.md](RENDER.md) for detailed instructions on deploying to Render.com.

## Accessing the Application

Once deployed, you can access the application at:
- Main frontend: `https://your-render-url.onrender.com/`
- Books API: `https://your-render-url.onrender.com/api/books`
- Products API: `https://your-render-url.onrender.com/api/products`

## API Endpoints

- `GET /` - Frontend interface
- `GET /api/books` - Retrieve all books in the library
- `GET /api/products` - Retrieve all products

## Database Schema

The application works with the existing database schema and adds:
- Books table with detailed information about library books
- Products table with information about products
- Related tables for departments, categories, users, etc.

## Features

- Connects to remote MySQL database
- Retrieves book and product information through REST API
- Inserts dummy data if tables are empty
- Handles existing database constraints properly
- Creates new tables as needed
- Provides a responsive web frontend

## Dummy Data

The application automatically inserts sample data:
- 3 sample books in the books table
- 5 sample products in the products table