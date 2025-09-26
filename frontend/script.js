// API endpoints
const API_BASE_URL = '/api';  // Using relative paths for the same domain
const BOOKS_API = `${API_BASE_URL}/books`;
const PRODUCTS_API = `${API_BASE_URL}/products`;

// DOM elements
const booksContainer = document.getElementById('books-container');
const productsContainer = document.getElementById('products-container');
const booksLoading = document.getElementById('books-loading');
const productsLoading = document.getElementById('products-loading');
const booksError = document.getElementById('books-error');
const productsError = document.getElementById('products-error');

// Fetch books from API
async function fetchBooks() {
    try {
        booksLoading.style.display = 'block';
        booksError.style.display = 'none';
        
        const response = await fetch(BOOKS_API);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        displayBooks(data.books);
    } catch (error) {
        console.error('Error fetching books:', error);
        booksError.style.display = 'block';
    } finally {
        booksLoading.style.display = 'none';
    }
}

// Fetch products from API
async function fetchProducts() {
    try {
        productsLoading.style.display = 'block';
        productsError.style.display = 'none';
        
        const response = await fetch(PRODUCTS_API);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        displayProducts(data.products);
    } catch (error) {
        console.error('Error fetching products:', error);
        productsError.style.display = 'block';
    } finally {
        productsLoading.style.display = 'none';
    }
}

// Display books in the UI
function displayBooks(books) {
    if (!books || books.length === 0) {
        booksContainer.innerHTML = '<p>No books available.</p>';
        return;
    }
    
    booksContainer.innerHTML = books.map(book => `
        <div class="card">
            <div class="card-header">
                <h3>${book.name}</h3>
            </div>
            <div class="card-body">
                <p><strong>Author:</strong> ${book.author}</p>
                <p><strong>ISBN:</strong> ${book.isbn}</p>
                <p><strong>Published Year:</strong> ${book.published_year}</p>
                <p><strong>Category:</strong> ${book.category}</p>
                <p><strong>Availability:</strong> 
                    <span class="${book.availability === 'available' ? 'available' : 'checked-out'}">
                        ${book.availability}
                    </span>
                </p>
            </div>
        </div>
    `).join('');
}

// Display products in the UI
function displayProducts(products) {
    if (!products || products.length === 0) {
        productsContainer.innerHTML = '<p>No products available.</p>';
        return;
    }
    
    productsContainer.innerHTML = products.map(product => `
        <div class="card">
            <div class="card-header">
                <h3>${product.name}</h3>
            </div>
            <div class="card-body">
                <p><strong>Price:</strong> $${product.price}</p>
                <p><strong>Category:</strong> ${product.category}</p>
                <p><strong>Stock:</strong> ${product.stock_quantity} units</p>
                ${product.description ? `<p><strong>Description:</strong> ${product.description}</p>` : ''}
                ${product.image_url ? `<p><strong>Image:</strong> <a href="${product.image_url}" target="_blank">View Image</a></p>` : ''}
            </div>
        </div>
    `).join('');
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
            
            // Update active nav link
            document.querySelectorAll('.nav-links a').forEach(link => {
                link.classList.remove('active');
            });
            this.classList.add('active');
        }
    });
});

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    // Fetch data when the page loads
    fetchBooks();
    fetchProducts();
    
    // Set active nav link based on current section
    const sections = document.querySelectorAll('.content-section');
    const navLinks = document.querySelectorAll('.nav-links a');
    
    window.addEventListener('scroll', () => {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (pageYOffset >= (sectionTop - 100)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
});