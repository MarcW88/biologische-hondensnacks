/* ========================================
   BIOLOGISCHE HONDENSNACKS - SHOP FUNCTIONALITY
   Reconstruction complète - Version propre
   ======================================== */

// Configuration
let currentPage = 1;
let productsPerPage = 12;
let filteredProducts = [];
let activeFilters = {
    search: '',
    categories: [],
    brands: [],
    ages: [],
    sizes: [],
    priceRange: { min: 0, max: 100 }
};

// Product data - Charge depuis window.PAGINATION_CONFIG si disponible
let allProducts = [];

// PRIORITÉ: Utiliser window.PAGINATION_CONFIG si disponible (pagination)
if (typeof window !== 'undefined' && window.PAGINATION_CONFIG && window.PAGINATION_CONFIG.products) {
    console.log('📄 Utilisation de PAGINATION_CONFIG');
    allProducts = window.PAGINATION_CONFIG.products.map(p => ({
        id: p.id,
        name: p.name,
        brand: p.brand,
        category: p.category || 'kauwsnacks',
        price: p.price,
        image: p.image,
        description: p.description,
        weight: p.weight,
        age: p.age || ["alle leeftijden"],
        size: p.size || ["alle maten"],
        features: p.features || ["natuurlijk"],
        inStock: p.inStock !== false,
        rating: p.rating || 4.5,
        reviews: p.reviewCount || 25,
        url: p.productUrl || p.url  // Utiliser productUrl en priorité
    }));
    console.log(`✅ ${allProducts.length} produits chargés depuis PAGINATION_CONFIG`);
} else {
    // FALLBACK: Liste hard-codée pour développement local
    console.log('📦 Utilisation de la liste hard-codée');
    allProducts = [
    {
        id: 1,
        name: "Chewpi Kauwstaaf (20+ kg) - Extra Large",
        brand: "Chewpi",
        category: "kauwsnacks",
        price: 15.99,
        image: "../images/Chewpi Kauwstaaf (20+ kg) - Extra Large.jpg",
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
        image: "../images/Chewpi Kauwstaaf (<5 kg) - Small 4-pack .jpg",
        description: "Chewpi Kauwstaaf (<5 kg) - Small 4-pack van Chewpi. Voor kleine honden (<5kg)",
        weight: "120 g",
        age: ["alle leeftijden"],
        size: ["klein"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/chewpi-kauwstaaf-5-kg-small-4-pack.html"
    },
    {
        id: 3,
        name: "Chewpi Kauwstaaf (5-10kg) - Medium 3-pack",
        brand: "Chewpi",
        category: "kauwsnacks",
        price: 17.99,
        image: "../images/Chewpi Kauwstaaf (5-10kg) - Medium 3-pack .jpg",
        description: "Chewpi Kauwstaaf (5-10kg) - Medium 3-pack van Chewpi. Himalaya traditie",
        weight: "180 g",
        age: ["alle leeftijden"],
        size: ["medium"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/chewpi-kauwstaaf-5-10kg-medium-3-pack.html"
    },
    {
        id: 4,
        name: "Chewpi Kauwstaaf (10-20kg) - Large 2-pack",
        brand: "Chewpi",
        category: "kauwsnacks",
        price: 14.99,
        image: "../images/Chewpi Kauwstaaf (10-20kg) - Large 2-pack .jpg",
        description: "Chewpi Kauwstaaf (10-20kg) - Large 2-pack van Chewpi. Voor middelgrote honden",
        weight: "240 g",
        age: ["alle leeftijden"],
        size: ["groot"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/chewpi-kauwstaaf-10-20kg-large-2-pack.html"
    },
    {
        id: 5,
        name: "Landman Eendfilet Gedroogd",
        brand: "Landman Hoevelaken",
        category: "natuurlijk",
        price: 21.5,
        image: "../images/Landman Eendfilet Gedroogd .jpg",
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
        id: 6,
        name: "HobbyFirst Canex Trainers Konijn",
        brand: "Hobbyfirst",
        category: "training",
        price: 18.0,
        image: "../images/HobbyFirst Canex Trainers Konijn .jpg",
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
        id: 7,
        name: "Softies Eend",
        brand: "Softies",
        category: "zachte snacks",
        price: 12.95,
        image: "../images/Softies Eend .jpg",
        description: "Softies Eend van Softies. Zachte snacks voor honden",
        weight: "200 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["zacht"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/softies-eend.html"
    },
    {
        id: 8,
        name: "BROK Verjaardag Snackpakket",
        brand: "BROK",
        category: "cadeaupakketten",
        price: 24.99,
        image: "../images/BROK Verjaardag Snackpakket .jpg",
        description: "BROK Verjaardag Snackpakket van BROK. Speciaal verjaardag pakket",
        weight: "500 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["cadeau"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/brok-verjaardag-snackpakket.html"
    },
    {
        id: 9,
        name: "Petstyle Living Sticks Kip 100 stuks",
        brand: "Petstyle Living",
        category: "training",
        price: 19.95,
        image: "../images/Petstyle Living Sticks Kip 100 stuks .jpg",
        description: "Petstyle Living Sticks Kip 100 stuks van Petstyle Living. Training sticks",
        weight: "300 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["training"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-sticks-kip-100-stuks.html"
    },
    {
        id: 10,
        name: "Petstyle Living Sticks Eend 100 stuks",
        brand: "Petstyle Living",
        category: "training",
        price: 21.95,
        image: "../images/Petstyle Living Sticks Eend 100 stuks .jpg",
        description: "Petstyle Living Sticks Eend 100 stuks van Petstyle Living. Training sticks eend",
        weight: "300 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["training"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-sticks-eend-100-stuks.html"
    },
    {
        id: 11,
        name: "Petstyle Living Sticks Kip & Rund 100 stuks",
        brand: "Petstyle Living",
        category: "training",
        price: 20.95,
        image: "../images/Petstyle Living Sticks Kip & Rund 100 stuks .jpg",
        description: "Petstyle Living Sticks Kip & Rund 100 stuks van Petstyle Living. Mix training sticks",
        weight: "300 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["training"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-sticks-kip-rund-100-stuks.html"
    },
    {
        id: 12,
        name: "Petstyle Living Kipfilet",
        brand: "Petstyle Living",
        category: "natuurlijk",
        price: 29.95,
        image: "../images/Petstyle Living Kipfilet .jpg",
        description: "Petstyle Living Kipfilet van Petstyle Living. Puur kipfilet",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-kipfilet.html"
    }
];

// Ajouter les autres produits (13-67)
const additionalProducts = [];
for (let i = 13; i <= 67; i++) {
    const brands = ['Renske', 'Beeztees', 'Trixie', 'Zukes', 'Hills', 'Royal Canin', 'Carnilove', 'Acana'];
    const categories = ['natuurlijk', 'training', 'kauwsnacks', 'puppy', 'senior'];
    const features = ['natuurlijk', 'premium', 'hypoallergeen', 'graanvrij', 'biologisch'];
    
    const brand = brands[Math.floor(Math.random() * brands.length)];
    const category = categories[Math.floor(Math.random() * categories.length)];
    const feature = features[Math.floor(Math.random() * features.length)];
    const price = parseFloat((Math.random() * 25 + 5).toFixed(2));
    const rating = parseFloat((4.0 + Math.random() * 1).toFixed(1));
    const reviews = Math.floor(Math.random() * 100) + 10;
    
    additionalProducts.push({
        id: i,
        name: `Biologische Hondensnack ${i}`,
        brand: brand,
        category: category,
        price: price,
        image: "../images/gezonde-kauwsnacks.jpg",
        description: `Natuurlijke hondensnack ${i} van ${brand} - 100% biologisch en gezond`,
        weight: "200 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: [feature],
        inStock: true,
        rating: rating,
        reviews: reviews,
        url: `../produits/biologische-hondensnack-${i}.html`
    });
}

    // Combiner tous les produits
    allProducts.push(...additionalProducts);
}

// Utility Functions
function generateStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;
    let stars = '';
    
    for (let i = 0; i < fullStars; i++) {
        stars += '★';
    }
    
    if (hasHalfStar) {
        stars += '☆';
    }
    
    return stars;
}

// Render Functions
function renderProducts() {
    console.log('🎨 Rendering products...');
    const productsGrid = document.getElementById('productsGrid');
    
    if (!productsGrid) {
        console.error('❌ Products grid element not found!');
        return;
    }
    
    const startIndex = (currentPage - 1) * productsPerPage;
    const endIndex = startIndex + productsPerPage;
    const productsToShow = filteredProducts.slice(0, endIndex);
    
    if (productsToShow.length === 0) {
        productsGrid.innerHTML = '<p>Geen producten gevonden.</p>';
        return;
    }
    
    productsGrid.innerHTML = productsToShow.map(product => `
        <div class="product-card" data-product-id="${product.id}">
            <img src="${product.image}" alt="${product.name}" class="product-image" loading="lazy">
            
            <div class="product-info">
                <div class="product-brand">${product.brand}</div>
                <h3 class="product-name">${product.name}</h3>
                <p class="product-description">${product.description}</p>
                
                <div class="product-features">
                    ${product.features.slice(0, 3).map(feature => `<span class="feature-tag">${feature}</span>`).join('')}
                </div>
                
                <div class="product-rating">
                    <span class="stars">${generateStars(product.rating)}</span>
                    <span class="rating-text">${product.rating.toFixed(1)} (${product.reviews} reviews)</span>
                </div>
                
                <div class="product-price">
                    <span class="price-current">€${product.price.toFixed(2)}</span>
                    <span class="price-per-unit">${product.weight}</span>
                </div>
            </div>
            
            <div class="product-actions">
                <div class="product-buttons">
                    <a href="${product.url}" class="btn-secondary btn-details">
                        👁️ Details bekijken
                    </a>
                    <a href="https://www.bol.com/nl/s/?searchtext=${encodeURIComponent(product.name)}" target="_blank" rel="noopener" class="btn-primary">
                        🛒 Bestel bij bol.com
                    </a>
                </div>
            </div>
            
            ${!product.inStock ? '<div class="out-of-stock">Tijdelijk uitverkocht</div>' : ''}
        </div>
    `).join('');
    
    updateLoadMoreButton();
}

function updateResultsCount() {
    const count = filteredProducts.length;
    const resultsCountElement = document.getElementById('resultsCount');
    if (resultsCountElement) {
        resultsCountElement.textContent = count + ' producten';
    }
    
    // Show/hide empty state
    const emptyState = document.getElementById('emptyState');
    const productsGrid = document.getElementById('productsGrid');
    
    if (count === 0) {
        if (emptyState) emptyState.style.display = 'block';
        if (productsGrid) productsGrid.style.display = 'grid';
    } else {
        if (emptyState) emptyState.style.display = 'none';
        if (productsGrid) productsGrid.style.display = 'grid';
    }
}

function updateLoadMoreButton() {
    const loadMoreContainer = document.getElementById('loadMoreContainer');
    if (!loadMoreContainer) return;
    
    const totalShown = currentPage * productsPerPage;
    const hasMore = totalShown < filteredProducts.length;
    
    loadMoreContainer.style.display = hasMore ? 'block' : 'none';
}

// Filter Functions
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
        if (activeFilters.brands.length > 0 && !activeFilters.brands.includes(product.brand)) {
            return false;
        }
        
        // Age filter
        if (activeFilters.ages.length > 0) {
            const hasMatchingAge = activeFilters.ages.some(age => product.age.includes(age));
            if (!hasMatchingAge) return false;
        }
        
        // Size filter
        if (activeFilters.sizes.length > 0) {
            const hasMatchingSize = activeFilters.sizes.some(size => product.size.includes(size));
            if (!hasMatchingSize) return false;
        }
        
        // Price filter
        if (product.price < activeFilters.priceRange.min || product.price > activeFilters.priceRange.max) {
            return false;
        }
        
        return true;
    });
    
    currentPage = 1;
    renderProducts();
    updateResultsCount();
}

// Event Handlers
function loadMoreProducts() {
    currentPage++;
    renderProducts();
}

function toggleFilter(type, value) {
    if (!activeFilters[type]) return;
    
    const index = activeFilters[type].indexOf(value);
    if (index > -1) {
        activeFilters[type].splice(index, 1);
    } else {
        activeFilters[type].push(value);
    }
    
    applyFilters();
}

// Initialize shop when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Shop initialization starting...');
    console.log('📦 Total products:', allProducts.length);
    
    // Initialize with all products
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
    
    console.log('✅ Shop initialized successfully!');
});
