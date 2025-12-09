/* ========================================
   PRODUCT PAGES GENERATOR
   Génère une page individuelle pour chaque produit
   ======================================== */

const fs = require('fs');
const path = require('path');

function generateProductPages() {
    console.log('📄 Génération des pages produits individuelles...\n');
    
    // Charger le catalogue
    const catalogPath = 'winkel/products-catalog.json';
    const products = JSON.parse(fs.readFileSync(catalogPath, 'utf8'));
    
    console.log(`🎯 ${products.length} pages produits à générer\n`);
    
    // Créer le dossier produits s'il n'existe pas
    const productsDir = 'produits';
    if (!fs.existsSync(productsDir)) {
        fs.mkdirSync(productsDir, { recursive: true });
    }
    
    let generatedCount = 0;
    
    products.forEach(product => {
        const slug = generateSlug(product.name);
        const filename = `${slug}.html`;
        const filepath = path.join(productsDir, filename);
        
        const pageContent = generateProductPageHTML(product, products);
        
        fs.writeFileSync(filepath, pageContent, 'utf8');
        generatedCount++;
        
        console.log(`✅ ${filename}`);
    });
    
    console.log(`\n🎉 ${generatedCount} pages produits générées dans /${productsDir}/`);
    
    // Générer l'index des produits
    generateProductsIndex(products);
    
    return generatedCount;
}

function generateSlug(name) {
    return name
        .toLowerCase()
        .replace(/[^a-z0-9\s]/g, '')
        .replace(/\s+/g, '-')
        .substring(0, 60);
}

function generateProductPageHTML(product, allProducts) {
    const slug = generateSlug(product.name);
    const relatedProducts = getRelatedProducts(product, allProducts, 4);
    
    return `<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${product.name} | ${product.brand} | Biologische Hondensnacks</title>
    <meta name="description" content="${product.description} ✓ ${product.brand} ✓ ${formatPrice(product.price)} ✓ Gratis verzending vanaf €20 via bol.com">
    <meta name="keywords" content="${generateKeywords(product)}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="${product.name} | ${product.brand}">
    <meta property="og:description" content="${product.description}">
    <meta property="og:image" content="${product.image}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="https://biologische-hondensnacks.nl/produits/${slug}.html">
    
    <!-- Product Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "${product.name}",
        "brand": {
            "@type": "Brand",
            "name": "${product.brand}"
        },
        "description": "${product.description}",
        "image": "${product.image}",
        "offers": {
            "@type": "Offer",
            "price": "${product.price}",
            "priceCurrency": "EUR",
            "availability": "${product.inStock ? 'https://schema.org/InStock' : 'https://schema.org/OutOfStock'}",
            "seller": {
                "@type": "Organization",
                "name": "bol.com"
            }
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "${product.rating}",
            "reviewCount": "${product.reviewCount}"
        },
        "category": "${getCategoryLabel(product.category)}"
    }
    </script>
    
    <!-- Styles -->
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="product-page.css">
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="../">🐕 Biologische Hondensnacks</a>
                </div>
                
                <nav class="nav">
                    <ul>
                        <li><a href="../">Home</a></li>
                        <li><a href="../natuurlijke-hondensnacks/">Natuurlijke Snacks</a></li>
                        <li><a href="../beste-hondensnacks-2024/">Top 10 Beste</a></li>
                        <li><a href="../winkel/">🛍️ Winkel</a></li>
                        <li><a href="../blog/">Blog</a></li>
                        <li><a href="../over-ons/">Over Ons</a></li>
                    </ul>
                </nav>
                
                <button class="mobile-menu-toggle">☰</button>
            </div>
        </div>
    </header>

    <!-- Breadcrumb -->
    <div class="breadcrumb">
        <div class="container">
            <a href="../">Home</a> > 
            <a href="../winkel/">Winkel</a> > 
            <a href="../winkel/?category=${product.category}">${getCategoryLabel(product.category)}</a> > 
            <span>${product.name}</span>
        </div>
    </div>

    <!-- Product Page -->
    <main class="product-page">
        <div class="container">
            <div class="product-layout">
                
                <!-- Product Images -->
                <div class="product-images">
                    <div class="main-image">
                        <img src="${product.image}" alt="${product.name}" id="mainImage">
                        ${generateBadges(product)}
                    </div>
                    
                    <!-- Thumbnail gallery (placeholder for multiple images) -->
                    <div class="image-thumbnails">
                        <img src="${product.image}" alt="${product.name}" class="thumbnail active" onclick="changeMainImage(this.src)">
                        <img src="${product.image}?variant=2" alt="${product.name} variant" class="thumbnail" onclick="changeMainImage(this.src)">
                        <img src="${product.image}?variant=3" alt="${product.name} packaging" class="thumbnail" onclick="changeMainImage(this.src)">
                    </div>
                </div>
                
                <!-- Product Info -->
                <div class="product-info">
                    <div class="product-header">
                        <div class="brand">${product.brand}</div>
                        <h1>${product.name}</h1>
                        
                        <div class="rating-section">
                            <div class="stars">${generateStars(product.rating)}</div>
                            <span class="rating-text">${product.rating}/5 (${product.reviewCount} reviews)</span>
                        </div>
                    </div>
                    
                    <div class="price-section">
                        <div class="price-main">
                            ${product.originalPrice ? `<span class="price-original">€${product.originalPrice.toFixed(2)}</span>` : ''}
                            <span class="price-current">€${product.price.toFixed(2)}</span>
                        </div>
                        <div class="price-per-unit">${product.pricePerUnit}</div>
                        ${product.originalPrice ? `<div class="savings">Bespaar €${(product.originalPrice - product.price).toFixed(2)}</div>` : ''}
                    </div>
                    
                    <div class="product-description">
                        <h3>Productbeschrijving</h3>
                        <p>${product.description}</p>
                    </div>
                    
                    <div class="product-features">
                        <h3>Eigenschappen</h3>
                        <div class="features-grid">
                            ${product.features.map(feature => `
                                <div class="feature-item">
                                    <span class="feature-icon">${getFeatureIcon(feature)}</span>
                                    <span class="feature-text">${getFeatureLabel(feature)}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                    
                    <div class="product-specs">
                        <h3>Specificaties</h3>
                        <div class="specs-table">
                            <div class="spec-row">
                                <span class="spec-label">Merk:</span>
                                <span class="spec-value">${product.brand}</span>
                            </div>
                            <div class="spec-row">
                                <span class="spec-label">Gewicht:</span>
                                <span class="spec-value">${product.weight}</span>
                            </div>
                            <div class="spec-row">
                                <span class="spec-label">Geschikt voor:</span>
                                <span class="spec-value">${product.age.map(age => getAgeLabel(age)).join(', ')}</span>
                            </div>
                            <div class="spec-row">
                                <span class="spec-label">Hondengrootte:</span>
                                <span class="spec-value">${product.size.map(size => getSizeLabel(size)).join(', ')}</span>
                            </div>
                            <div class="spec-row">
                                <span class="spec-label">Ingrediënten:</span>
                                <span class="spec-value">${product.ingredients}</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Purchase Section -->
                    <div class="purchase-section">
                        <div class="stock-info">
                            ${product.inStock ? 
                                `<span class="in-stock">✓ Op voorraad</span>` : 
                                `<span class="out-of-stock">⚠️ Tijdelijk uitverkocht</span>`
                            }
                            ${product.fastDelivery ? `<span class="fast-delivery">🚚 Morgen in huis</span>` : ''}
                        </div>
                        
                        <div class="purchase-actions">
                            <a href="${product.bolUrl}" target="_blank" rel="noopener" class="btn-primary btn-large" onclick="trackPurchaseClick('${product.id}', '${product.name}')">
                                🛒 Bestel nu bij bol.com
                            </a>
                            
                            <div class="secondary-actions">
                                <button class="btn-secondary" onclick="addToWishlist(${product.id})">
                                    ❤️ Toevoegen aan verlanglijst
                                </button>
                                <button class="btn-secondary" onclick="shareProduct()">
                                    📤 Delen
                                </button>
                            </div>
                        </div>
                        
                        <div class="trust-badges">
                            <div class="trust-item">
                                <span>🚚</span>
                                <span>Gratis verzending vanaf €20</span>
                            </div>
                            <div class="trust-item">
                                <span>↩️</span>
                                <span>30 dagen retourrecht</span>
                            </div>
                            <div class="trust-item">
                                <span>⭐</span>
                                <span>4.8/5 klanttevredenheid</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Related Products -->
            <section class="related-products">
                <h2>Gerelateerde producten</h2>
                <div class="products-grid">
                    ${relatedProducts.map(relatedProduct => generateProductCard(relatedProduct)).join('')}
                </div>
            </section>
            
            <!-- Reviews Section -->
            <section class="reviews-section">
                <h2>Klantbeoordelingen</h2>
                <div class="reviews-summary">
                    <div class="rating-overview">
                        <div class="rating-large">${product.rating}</div>
                        <div class="stars-large">${generateStars(product.rating)}</div>
                        <div class="review-count">${product.reviewCount} beoordelingen</div>
                    </div>
                </div>
                
                <div class="sample-reviews">
                    ${generateSampleReviews(product)}
                </div>
                
                <div class="reviews-cta">
                    <p>Meer reviews lezen? Bekijk alle beoordelingen op bol.com</p>
                    <a href="${product.bolUrl}#reviews" target="_blank" class="btn-secondary">
                        Alle reviews bekijken
                    </a>
                </div>
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <div class="logo">🐕 Biologische Hondensnacks</div>
                    <p>De beste biologische en natuurlijke hondensnacks van Nederland.</p>
                </div>
                
                <div class="footer-section">
                    <h4>Populaire Categorieën</h4>
                    <ul>
                        <li><a href="../natuurlijke-hondensnacks/">Natuurlijke Snacks</a></li>
                        <li><a href="../winkel/?category=puppy">Puppy Snacks</a></li>
                        <li><a href="../winkel/?category=training">Training Snacks</a></li>
                        <li><a href="../winkel/?category=dental">Dental Care</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4>Support</h4>
                    <ul>
                        <li><a href="../over-ons/">Over Ons</a></li>
                        <li><a href="#contact">Contact</a></li>
                        <li><a href="#faq">Veelgestelde Vragen</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4>Blijf op de hoogte</h4>
                    <div class="newsletter">
                        <input type="email" placeholder="Je e-mailadres">
                        <button>Aanmelden</button>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 Biologische Hondensnacks. Alle rechten voorbehouden.</p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="../js/main.js"></script>
    <script src="product-page.js"></script>
</body>
</html>`;
}

function generateBadges(product) {
    if (!product.badges || product.badges.length === 0) return '';
    
    return `<div class="product-badges">
        ${product.badges.map(badge => `<span class="badge badge-${badge}">${getBadgeLabel(badge)}</span>`).join('')}
    </div>`;
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

function generateProductCard(product) {
    const slug = generateSlug(product.name);
    
    return `
        <div class="product-card">
            <a href="${slug}.html" class="product-link">
                <img src="${product.image}" alt="${product.name}" class="product-image">
                <div class="product-info">
                    <div class="product-brand">${product.brand}</div>
                    <h3 class="product-name">${product.name}</h3>
                    <div class="product-rating">
                        <span class="stars">${generateStars(product.rating)}</span>
                        <span class="rating-text">${product.rating}</span>
                    </div>
                    <div class="product-price">€${product.price.toFixed(2)}</div>
                </div>
            </a>
        </div>
    `;
}

function generateSampleReviews(product) {
    const sampleReviews = [
        {
            name: "Sandra M.",
            rating: 5,
            text: "Mijn hond is er dol op! Gezonde ingrediënten en hij vindt ze heerlijk.",
            date: "2 weken geleden"
        },
        {
            name: "Peter K.",
            rating: 4,
            text: "Goede kwaliteit snacks. Mijn hond reageert er goed op tijdens training.",
            date: "1 maand geleden"
        },
        {
            name: "Lisa V.",
            rating: 5,
            text: "Eindelijk snacks waar mijn gevoelige hond geen last van heeft. Aanrader!",
            date: "3 weken geleden"
        }
    ];
    
    return sampleReviews.map(review => `
        <div class="review-item">
            <div class="review-header">
                <span class="reviewer-name">${review.name}</span>
                <div class="review-rating">${generateStars(review.rating)}</div>
                <span class="review-date">${review.date}</span>
            </div>
            <p class="review-text">${review.text}</p>
        </div>
    `).join('');
}

function getRelatedProducts(product, allProducts, limit = 4) {
    return allProducts
        .filter(p => p.id !== product.id)
        .filter(p => p.category === product.category || p.brand === product.brand)
        .sort((a, b) => b.rating - a.rating)
        .slice(0, limit);
}

function generateKeywords(product) {
    return [
        product.name,
        product.brand,
        product.category,
        ...product.features,
        'biologische hondensnacks',
        'natuurlijke hondensnacks',
        'bol.com'
    ].join(', ');
}

function formatPrice(price) {
    return `€${price.toFixed(2)}`;
}

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
        'hypoallergeen': '💚',
        'duurzaam': '♻️'
    };
    return icons[feature] || '✓';
}

function getFeatureLabel(feature) {
    const labels = {
        'biologisch': 'Biologisch',
        'natuurlijk': 'Natuurlijk',
        'graanvrij': 'Graanvrij',
        'glutenvrij': 'Glutenvrij',
        'hypoallergeen': 'Hypoallergeen',
        'duurzaam': 'Duurzaam'
    };
    return labels[feature] || feature;
}

function getAgeLabel(age) {
    const labels = {
        'puppy': 'Puppy',
        'adult': 'Volwassen',
        'senior': 'Senior'
    };
    return labels[age] || age;
}

function getSizeLabel(size) {
    const labels = {
        'small': 'Klein',
        'medium': 'Middel',
        'large': 'Groot'
    };
    return labels[size] || size;
}

function generateProductsIndex(products) {
    const indexContent = `<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alle Producten | Biologische Hondensnacks</title>
    <meta name="description" content="Bekijk alle ${products.length} biologische hondensnacks. Van training snacks tot kauwsnacks - alles voor je hond.">
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="../">🐕 Biologische Hondensnacks</a>
                </div>
                <nav class="nav">
                    <ul>
                        <li><a href="../">Home</a></li>
                        <li><a href="../winkel/">🛍️ Winkel</a></li>
                        <li><a href="../blog/">Blog</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>
    
    <main class="container">
        <h1>Alle Producten (${products.length})</h1>
        <div class="products-grid">
            ${products.map(product => generateProductCard(product)).join('')}
        </div>
    </main>
</body>
</html>`;
    
    fs.writeFileSync('produits/index.html', indexContent, 'utf8');
    console.log('✅ Index des produits créé: /produits/index.html');
}

// Exécuter la génération
if (require.main === module) {
    generateProductPages();
}

module.exports = { generateProductPages };
