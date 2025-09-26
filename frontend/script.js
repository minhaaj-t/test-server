// DOM elements
const booksBtn = document.getElementById('books-btn');
const productsBtn = document.getElementById('products-btn');
const booksSection = document.getElementById('books-section');
const productsSection = document.getElementById('products-section');
const booksContainer = document.getElementById('books-container');
const productsContainer = document.getElementById('products-container');

// Event listeners for navigation buttons
booksBtn.addEventListener('click', () => {
    showSection('books');
});

productsBtn.addEventListener('click', () => {
    showSection('products');
});

// Function to show the selected section
function showSection(section) {
    // Update active button
    booksBtn.classList.toggle('active', section === 'books');
    productsBtn.classList.toggle('active', section === 'products');
    
    // Show active section
    booksSection.classList.toggle('active', section === 'books');
    productsSection.classList.toggle('active', section === 'products');
    
    // Load data if not already loaded
    if (section === 'books' && booksContainer.querySelector('.loading')) {
        loadBooks();
    } else if (section === 'products' && productsContainer.querySelector('.loading')) {
        loadProducts();
    }
}

// Function to load books from the API
async function loadBooks() {
    try {
        // Use absolute path for API endpoint
        const response = await fetch('/api/books');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayBooks(data.books);
    } catch (error) {
        console.error('Error loading books:', error);
        booksContainer.innerHTML = `<div class="error">Failed to load books: ${error.message}</div>`;
    }
}

// Function to display books
function displayBooks(books) {
    if (books.length === 0) {
        booksContainer.innerHTML = '<div class="loading">No books found in the library.</div>';
        return;
    }
    
    booksContainer.innerHTML = books.map(book => `
        <div class="item-card">
            <div class="item-card-header">
                <h3>${book.name}</h3>
                <p>by ${book.author}</p>
            </div>
            <div class="item-card-body">
                <p><strong>ISBN:</strong> ${book.isbn}</p>
                <p><strong>Published:</strong> ${book.published_year}</p>
                <p><strong>Availability:</strong> 
                    <span class="${book.availability === 'available' ? 'available' : 'checked-out'}">
                        ${book.availability}
                    </span>
                </p>
                <p><strong>Category:</strong> ${book.category}</p>
            </div>
        </div>
    `).join('');
}

// Function to load products from the API
async function loadProducts() {
    try {
        // Use absolute path for API endpoint
        const response = await fetch('/api/products');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayProducts(data.products);
    } catch (error) {
        console.error('Error loading products:', error);
        productsContainer.innerHTML = `<div class="error">Failed to load products: ${error.message}</div>`;
    }
}

// Function to display products
function displayProducts(products) {
    if (products.length === 0) {
        productsContainer.innerHTML = '<div class="loading">No products found in the store.</div>';
        return;
    }
    
    productsContainer.innerHTML = products.map(product => `
        <div class="item-card">
            <div class="item-card-header">
                <h3>${product.name}</h3>
                <p>$${product.price}</p>
            </div>
            <div class="item-card-body">
                <p>${product.description}</p>
                <p><strong>Category:</strong> ${product.category}</p>
                <p><strong>In Stock:</strong> ${product.stock_quantity} items</p>
                ${product.image_url ? `<img src="${product.image_url}" alt="${product.name}" style="width:100%;height:auto;margin-top:10px;">` : ''}
            </div>
        </div>
    `).join('');
}

// Initialize the page by showing books section
document.addEventListener('DOMContentLoaded', () => {
    showSection('books');
});