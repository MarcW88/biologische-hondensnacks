/* ========================================
   BIOLOGISCHE HONDENSNACKS - SHOP FUNCTIONALITY
   ======================================== */

// Product data from real catalog
const allProducts = [
    {
        id: 1,
        name: "Chewpi Kauwstaaf (20+ kg) - Extra Large",
        brand: "Chewpi",
        category: "kauwsnacks",
        price: 15.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Chewpi Kauwstaaf (20+ kg) - Extra Large van Chewpi. 100% natuurlijk, Belgisch",
        weight: "120 g",
        age: ["alle leeftijden"],
        size: ["groot"],
        features: ["natuurlijk"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/chewpi-kauwstaaf-20-kg-extra-large.html"
    },
    {
        id: 2,
        name: "Chewpi Kauwstaaf (<5 kg) - Small 4-pack",
        brand: "Chewpi",
        category: "kauwsnacks",
        price: 15.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Chewpi Kauwstaaf (<5 kg) - Small 4-pack van Chewpi. Voor kleine honden (<5kg)",
        weight: "120 g",
        age: ["alle leeftijden"],
        size: ["klein"],
        features: ["natuurlijk"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/chewpi-kauwstaaf-5-kg-small-4-pack.html"
    },
    {
        id: 3,
        name: "Landman Eendfilet Gedroogd",
        brand: "Landman Hoevelaken",
        category: "natuurlijk",
        price: 21.50,
        image: "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop",
        description: "Landman Eendfilet Gedroogd van Landman Hoevelaken. 100% natuurlijk, hypoallergeen",
        weight: "400 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk", "hypoallergeen"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/landman-eendfilet-gedroogd.html"
    },
    {
        id: 4,
        name: "HobbyFirst Canex Trainers Konijn",
        brand: "Hobbyfirst",
        category: "training",
        price: 18.00,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "HobbyFirst Canex Trainers Konijn van Hobbyfirst. Pure Trainers, supplement",
        weight: "250 g",
        age: ["puppy"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/hobbyfirst-canex-trainers-konijn.html"
    },
    {
        id: 5,
        name: "Softies Eend",
        brand: "Bellobox",
        category: "training",
        price: 8.50,
        image: "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop",
        description: "Softies Eend van Bellobox. Ideaal voor training",
        weight: "100 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/softies-eend.html"
    }
];
let filteredProducts = [...allProducts];
let currentPage = 1;
const productsPerPage = 12;
let activeFilters = {
    search: '',
    categories: [],
    brands: [],
    ages: [],
    sizes: [],
    features: [],
    maxPrice: 50
};

// Sample product data (to be replaced with actual catalog data)
const sampleProducts = [
    {
        id: 1,
        name: "Yarrah Biologische Kip & Rund Trainingssnacks",
        brand: "Yarrah",
        price: 8.95,
        originalPrice: null,
        pricePerUnit: "€4.48 per 100g",
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        rating: 4.8,
        reviewCount: 156,
        description: "100% biologische trainingssnacks met kip en rund. Perfect voor training en beloning.",
        category: "training",
        age: ["puppy", "adult"],
        size: ["small", "medium", "large"],
        features: ["biologisch", "natuurlijk", "graanvrij"],
        badges: ["bestseller", "bio"],
        bolUrl: "https://www.bol.com/nl/p/yarrah-biologische-trainingssnacks/123456789/",
        inStock: true,
        fastDelivery: true
    },
    {
        id: 2,
        name: "Lily's Kitchen Puppy Training Treats",
        brand: "Lily's Kitchen",
        price: 6.49,
        originalPrice: 7.99,
        pricePerUnit: "€6.49 per 100g",
        image: "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400&h=300&fit=crop",
        rating: 4.6,
        reviewCount: 89,
        description: "Natuurlijke puppy trainingssnacks met kip en zoete aardappel.",
        category: "puppy",
        age: ["puppy"],
        size: ["small", "medium"],
        features: ["natuurlijk", "graanvrij"],
        badges: ["new", "sale"],
        bolUrl: "https://www.bol.com/nl/p/lilys-kitchen-puppy-treats/123456790/",
        inStock: true,
        fastDelivery: true
    },
    {
        id: 3,
        name: "Green Petfood Dental Care Sticks",
        brand: "Green Petfood",
        price: 12.95,
        originalPrice: null,
        pricePerUnit: "€2.59 per stuk",
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        rating: 4.7,
        reviewCount: 234,
        description: "Duurzame kauwsticks voor gezonde tanden en tandvlees. Met insectenproteïne.",
        category: "dental",
        age: ["adult", "senior"],
        size: ["medium", "large"],
        features: ["natuurlijk", "duurzaam"],
        badges: ["bio"],
        bolUrl: "https://www.bol.com/nl/p/green-petfood-dental-sticks/123456791/",
        inStock: true,
        fastDelivery: false
    },
    {
        id: 4,
        name: "Zuke's Mini Naturals Zalm Training Treats",
        brand: "Zuke's",
        price: 9.95,
        originalPrice: null,
        pricePerUnit: "€9.95 per 170g",
        image: "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop",
        rating: 4.9,
        reviewCount: 312,
        description: "Mini trainingssnacks met echte zalm. Ideaal voor frequente beloningen.",
        category: "training",
        age: ["puppy", "adult"],
        size: ["small", "medium"],
        features: ["natuurlijk", "glutenvrij"],
        badges: ["bestseller"],
        bolUrl: "https://www.bol.com/nl/p/zukes-mini-naturals-zalm/123456792/",
        inStock: false,
        fastDelivery: false
    }
];

// Initialize shop
document.addEventListener('DOMContentLoaded', async function() {
    console.log('🛍️ Initialisation de la boutique...');
    
    try {
        // Charger les produits depuis le catalogue
        const response = await fetch('products-catalog.json');
        allProducts = await response.json();
        
        console.log(`✅ ${allProducts.length} produits chargés depuis le catalogue`);
        
        // Enrichir les données
        allProducts = allProducts.map(product => ({
            ...product,
            searchTerms: generateSearchTerms(product)
        }));
        
    } catch (error) {
        console.error('Erreur chargement catalogue:', error);
        console.log('📝 Utilisation des données de démonstration');
        allProducts = [...sampleProducts];
    }
    
    filteredProducts = [...allProducts];
    renderProducts();
    updateResultsCount();
    setupEventListeners();
    
    // Mettre à jour les compteurs de filtres
    updateFilterCounts();
});

// Setup event listeners
function setupEventListeners() {
    // Search input
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(handleSearch, 300));
    }
    
    // Mobile menu toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', toggleMobileMenu);
    }
}

// Debounce function for search
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Handle search
function handleSearch(event) {
    activeFilters.search = event.target.value.toLowerCase();
    applyFilters();
}

// Apply all filters
function applyFilters() {
    filteredProducts = allProducts.filter(product => {
        // Search filter
        if (activeFilters.search && !product.name.toLowerCase().includes(activeFilters.search) 
            && !product.brand.toLowerCase().includes(activeFilters.search)
            && !product.description.toLowerCase().includes(activeFilters.search)) {
            return false;
        }
        
        // Category filter
        if (activeFilters.categories.length > 0 && !activeFilters.categories.includes(product.category)) {
            return false;
        }
        
        // Brand filter
        if (activeFilters.brands.length > 0 && !activeFilters.brands.includes(product.brand.toLowerCase().replace(/[^a-z0-9]/g, '-'))) {
            return false;
        }
        
        // Age filter
        if (activeFilters.ages.length > 0 && !activeFilters.ages.some(age => product.age.includes(age))) {
            return false;
        }
        
        // Size filter
        if (activeFilters.sizes.length > 0 && !activeFilters.sizes.some(size => product.size.includes(size))) {
            return false;
        }
        
        // Features filter
        if (activeFilters.features.length > 0 && !activeFilters.features.some(feature => product.features.includes(feature))) {
            return false;
        }
        
        // Price filter
        if (product.price > activeFilters.maxPrice) {
            return false;
        }
        
        return true;
    });
    
    currentPage = 1;
    renderProducts();
    updateResultsCount();
    updateActiveFilters();
}

// Update price filter
function updatePriceFilter(value) {
    activeFilters.maxPrice = parseInt(value);
    document.getElementById('maxPrice').textContent = '€' + value;
    applyFilters();
}

// Clear all filters
function clearAllFilters() {
    // Reset filter object
    activeFilters = {
        search: '',
        categories: [],
        brands: [],
        ages: [],
        sizes: [],
        features: [],
        maxPrice: 50
    };
    
    // Reset UI
    document.getElementById('searchInput').value = '';
    document.getElementById('priceRange').value = 50;
    document.getElementById('maxPrice').textContent = '€50';
    
    // Uncheck all checkboxes
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(checkbox => {
        checkbox.checked = false;
    });
    
    // Apply filters
    applyFilters();
}

// Update results count
function updateResultsCount() {
    const count = filteredProducts.length;
    document.getElementById('resultsCount').textContent = count + ' producten';
    
    // Show/hide empty state
    const emptyState = document.getElementById('emptyState');
    const productsGrid = document.getElementById('productsGrid');
    
    if (count === 0) {
        emptyState.style.display = 'block';
        productsGrid.style.display = 'none';
    } else {
        emptyState.style.display = 'none';
        productsGrid.style.display = 'grid';
    }
}

// Update active filters display
function updateActiveFilters() {
    const activeFiltersContainer = document.getElementById('activeFilters');
    const filterTags = document.getElementById('filterTags');
    
    let tags = [];
    
    // Add search tag
    if (activeFilters.search) {
        tags.push({ type: 'search', value: activeFilters.search, label: `Zoeken: "${activeFilters.search}"` });
    }
    
    // Add category tags
    activeFilters.categories.forEach(category => {
        const label = getCategoryLabel(category);
        tags.push({ type: 'categories', value: category, label: label });
    });
    
    // Add brand tags
    activeFilters.brands.forEach(brand => {
        const label = getBrandLabel(brand);
        tags.push({ type: 'brands', value: brand, label: label });
    });
    
    // Add other filter tags
    [...activeFilters.ages, ...activeFilters.sizes, ...activeFilters.features].forEach(filter => {
        tags.push({ type: 'other', value: filter, label: getFilterLabel(filter) });
    });
    
    // Add price tag if not max
    if (activeFilters.maxPrice < 50) {
        tags.push({ type: 'price', value: activeFilters.maxPrice, label: `Max €${activeFilters.maxPrice}` });
    }
    
    if (tags.length > 0) {
        filterTags.innerHTML = tags.map(tag => `
            <span class="filter-tag">
                ${tag.label}
                <span class="remove" onclick="removeFilter('${tag.type}', '${tag.value}')">×</span>
            </span>
        `).join('');
        activeFiltersContainer.style.display = 'flex';
    } else {
        activeFiltersContainer.style.display = 'none';
    }
}

// Remove individual filter
function removeFilter(type, value) {
    switch(type) {
        case 'search':
            activeFilters.search = '';
            document.getElementById('searchInput').value = '';
            break;
        case 'categories':
            activeFilters.categories = activeFilters.categories.filter(c => c !== value);
            break;
        case 'brands':
            activeFilters.brands = activeFilters.brands.filter(b => b !== value);
            break;
        case 'price':
            activeFilters.maxPrice = 50;
            document.getElementById('priceRange').value = 50;
            document.getElementById('maxPrice').textContent = '€50';
            break;
        default:
            // Handle ages, sizes, features
            activeFilters.ages = activeFilters.ages.filter(f => f !== value);
            activeFilters.sizes = activeFilters.sizes.filter(f => f !== value);
            activeFilters.features = activeFilters.features.filter(f => f !== value);
    }
    
    // Update corresponding checkboxes
    document.querySelectorAll(`input[value="${value}"]`).forEach(checkbox => {
        checkbox.checked = false;
    });
    
    applyFilters();
}

// Sort products
function sortProducts() {
    const sortValue = document.getElementById('sortSelect').value;
    
    switch(sortValue) {
        case 'price-low':
            filteredProducts.sort((a, b) => a.price - b.price);
            break;
        case 'price-high':
            filteredProducts.sort((a, b) => b.price - a.price);
            break;
        case 'rating':
            filteredProducts.sort((a, b) => b.rating - a.rating);
            break;
        case 'name':
            filteredProducts.sort((a, b) => a.name.localeCompare(b.name));
            break;
        case 'newest':
            filteredProducts.sort((a, b) => b.id - a.id);
            break;
        default: // popular
            filteredProducts.sort((a, b) => b.reviewCount - a.reviewCount);
    }
    
    renderProducts();
}

// Toggle view (grid/list)
function toggleView(view) {
    const productsGrid = document.getElementById('productsGrid');
    const viewBtns = document.querySelectorAll('.view-btn');
    
    viewBtns.forEach(btn => btn.classList.remove('active'));
    document.querySelector(`[data-view="${view}"]`).classList.add('active');
    
    if (view === 'list') {
        productsGrid.classList.add('list-view');
    } else {
        productsGrid.classList.remove('list-view');
    }
}

// Render products
function renderProducts() {
    const productsGrid = document.getElementById('productsGrid');
    const startIndex = (currentPage - 1) * productsPerPage;
    const endIndex = startIndex + productsPerPage;
    const productsToShow = filteredProducts.slice(0, endIndex);
    
    productsGrid.innerHTML = productsToShow.map(product => `
        <div class="product-card" data-product-id="${product.id}">
            <div class="product-badges">
                ${product.badges.map(badge => `<span class="product-badge badge-${badge}">${getBadgeLabel(badge)}</span>`).join('')}
            </div>
            
            <img src="${product.image}" alt="${product.name}" class="product-image" loading="lazy">
            
            <div class="product-info">
                <div class="product-brand">${product.brand}</div>
                <h3 class="product-name">${product.name}</h3>
                <p class="product-description">${product.description}</p>
                
                <div class="product-features">
                    ${product.features.slice(0, 3).map(feature => `<span class="feature-tag">${getFeatureIcon(feature)} ${getFilterLabel(feature)}</span>`).join('')}
                </div>
                
                <div class="product-rating">
                    <span class="stars">${generateStars(product.rating)}</span>
                    <span class="rating-text">${product.rating} (${product.reviewCount})</span>
                </div>
                
                <div class="product-price">
                    <span class="price-current">€${product.price.toFixed(2)}</span>
                    ${product.originalPrice ? `<span class="price-original">€${product.originalPrice.toFixed(2)}</span>` : ''}
                    <span class="price-per-unit">${product.pricePerUnit}</span>
                </div>
            </div>
            
            <div class="product-actions">
                <div class="product-buttons">
                    <a href="../produits/${generateSlug(product.name)}.html" class="btn-secondary btn-details">
                        👁️ Details bekijken
                    </a>
                    <a href="${product.bolUrl}" target="_blank" rel="noopener" class="btn-primary" onclick="trackClick('${product.id}', '${product.name}')">
                        🛒 Bestel bij bol.com
                    </a>
                </div>
                <button class="btn-secondary" onclick="toggleWishlist(${product.id})" title="Toevoegen aan verlanglijst">
                    ❤️
                </button>
            </div>
            
            ${!product.inStock ? '<div class="out-of-stock">Tijdelijk uitverkocht</div>' : ''}
            ${product.fastDelivery ? '<div class="fast-delivery">🚚 Morgen in huis</div>' : ''}
        </div>
    `).join('');
    
    // Update load more button
    updateLoadMoreButton();
}

// Load more products
function loadMoreProducts() {
    currentPage++;
    renderProducts();
}

// Update load more button
function updateLoadMoreButton() {
    const loadMoreContainer = document.getElementById('loadMoreContainer');
    const totalPages = Math.ceil(filteredProducts.length / productsPerPage);
    
    if (currentPage >= totalPages) {
        loadMoreContainer.style.display = 'none';
    } else {
        loadMoreContainer.style.display = 'block';
    }
}

// Track clicks for analytics
function trackClick(productId, productName) {
    // Analytics tracking would go here
    console.log(`Clicked product: ${productId} - ${productName}`);
    
    // You can add Google Analytics or other tracking here
    if (typeof gtag !== 'undefined') {
        gtag('event', 'click', {
            event_category: 'affiliate_link',
            event_label: productName,
            value: productId
        });
    }
}

// Toggle wishlist
function toggleWishlist(productId) {
    // Wishlist functionality
    let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    
    if (wishlist.includes(productId)) {
        wishlist = wishlist.filter(id => id !== productId);
        showNotification('Verwijderd uit verlanglijst', 'info');
    } else {
        wishlist.push(productId);
        showNotification('Toegevoegd aan verlanglijst', 'success');
    }
    
    localStorage.setItem('wishlist', JSON.stringify(wishlist));
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#28a745' : '#17a2b8'};
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Générer un slug pour les URLs
function generateSlug(name) {
    return name
        .toLowerCase()
        .replace(/[^a-z0-9\s]/g, '')
        .replace(/\s+/g, '-')
        .substring(0, 60);
}

// Générer des termes de recherche pour chaque produit
function generateSearchTerms(product) {
    const terms = [
        product.name.toLowerCase(),
        product.brand.toLowerCase(),
        product.description.toLowerCase(),
        product.category,
        ...product.features,
        ...product.age,
        ...product.size
    ];
    
    return terms.join(' ');
}

// Mettre à jour les compteurs de filtres
function updateFilterCounts() {
    // Compter les produits par catégorie
    const categoryCounts = {};
    const brandCounts = {};
    
    allProducts.forEach(product => {
        // Catégories
        categoryCounts[product.category] = (categoryCounts[product.category] || 0) + 1;
        
        // Marques
        const brandKey = product.brand.toLowerCase().replace(/[^a-z0-9]/g, '-');
        brandCounts[brandKey] = (brandCounts[brandKey] || 0) + 1;
    });
    
    // Mettre à jour les compteurs dans l'interface
    Object.entries(categoryCounts).forEach(([category, count]) => {
        const countElement = document.querySelector(`input[value="${category}"] + span + .count`);
        if (countElement) {
            countElement.textContent = `(${count})`;
        }
    });
    
    Object.entries(brandCounts).forEach(([brand, count]) => {
        const countElement = document.querySelector(`input[value="${brand}"] + span + .count`);
        if (countElement) {
            countElement.textContent = `(${count})`;
        }
    });
}

// Helper functions
function getCategoryLabel(category) {
    const labels = {
        'training': 'Training Snacks',
        'kauwsnacks': 'Kauwsnacks',
        'puppy': 'Puppy Snacks',
        'dental': 'Dental Care',
        'hypoallergeen': 'Hypoallergeen'
    };
    return labels[category] || category;
}

function getBrandLabel(brand) {
    return brand.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

function getFilterLabel(filter) {
    const labels = {
        'puppy': 'Puppy',
        'adult': 'Volwassen',
        'senior': 'Senior',
        'small': 'Klein',
        'medium': 'Middel',
        'large': 'Groot',
        'biologisch': 'Biologisch',
        'natuurlijk': 'Natuurlijk',
        'graanvrij': 'Graanvrij',
        'glutenvrij': 'Glutenvrij',
        'duurzaam': 'Duurzaam'
    };
    return labels[filter] || filter;
}

function getBadgeLabel(badge) {
    const labels = {
        'bestseller': 'Bestseller',
        'new': 'Nieuw',
        'bio': 'Bio',
        'sale': 'Aanbieding'
    };
    return labels[badge] || badge;
}

function getFeatureIcon(feature) {
    const icons = {
        'biologisch': '🌱',
        'natuurlijk': '🍃',
        'graanvrij': '🌾',
        'glutenvrij': '🚫',
        'duurzaam': '♻️'
    };
    return icons[feature] || '✓';
}

function generateStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 >= 0.5;
    let stars = '';
    
    for (let i = 0; i < fullStars; i++) {
        stars += '★';
    }
    
    if (hasHalfStar) {
        stars += '☆';
    }
    
    return stars;
}

// Mobile menu toggle
function toggleMobileMenu() {
    const nav = document.querySelector('.nav');
    nav.classList.toggle('mobile-open');
}

// CSS for animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .notification {
        animation: slideIn 0.3s ease;
    }
    
    .out-of-stock {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(220, 53, 69, 0.9);
        color: white;
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 600;
    }
    
    .fast-delivery {
        position: absolute;
        bottom: 8px;
        right: 8px;
        background: rgba(40, 167, 69, 0.9);
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 10px;
    }
`;
document.head.appendChild(style);

// Initialize shop when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize with sample products
    allProducts = sampleProducts;
    filteredProducts = [...allProducts];
    
    // Render initial products
    renderProducts();
    updateResultsCount();
    
    // Add event listeners for search
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            activeFilters.search = this.value.toLowerCase();
            applyFilters();
        });
    }
    
    // Add event listeners for filter checkboxes
    document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const filterType = this.getAttribute('data-filter-type');
            const filterValue = this.getAttribute('data-filter-value');
            
            if (this.checked) {
                if (!activeFilters[filterType].includes(filterValue)) {
                    activeFilters[filterType].push(filterValue);
                }
            } else {
                activeFilters[filterType] = activeFilters[filterType].filter(v => v !== filterValue);
            }
            
            applyFilters();
        });
    });
    
    // Add event listener for price range
    const priceRange = document.getElementById('priceRange');
    if (priceRange) {
        priceRange.addEventListener('input', function() {
            updatePriceFilter(this.value);
        });
    }
    
    // Add event listener for clear filters button
    const clearFiltersBtn = document.getElementById('clearFilters');
    if (clearFiltersBtn) {
        clearFiltersBtn.addEventListener('click', clearAllFilters);
    }
    
    console.log('Shop initialized with', allProducts.length, 'products');
});
