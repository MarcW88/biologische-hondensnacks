/* ========================================
   PRODUCT LOADER - Charge les produits du catalogue
   ======================================== */

// Charger les produits depuis le catalogue JSON
async function loadProductsFromCatalog() {
    try {
        // PRIORITÉ: Si pagination config existe, utiliser directement ces produits
        if (window.PAGINATION_CONFIG) {
            console.log(`📄 Page ${window.PAGINATION_CONFIG.currentPage}/${window.PAGINATION_CONFIG.totalPages}`);
            console.log(`📦 ${window.PAGINATION_CONFIG.products.length} produits sur cette page`);
            
            // Utiliser les produits de la page courante (déjà dans le HTML)
            const paginatedProducts = window.PAGINATION_CONFIG.products;
            
            // Enrichir les données
            return paginatedProducts.map(product => ({
                ...product,
                searchTerms: generateSearchTerms(product),
                isNew: isNewProduct(product),
                isPopular: product.reviewCount > 200,
                isBestseller: product.badges && product.badges.includes('bestseller'),
                bolUrl: ensureBolUrl(product.bolUrl, product),
                deliveryInfo: getDeliveryInfo(product)
            }));
        }
        
        // Sinon charger depuis le JSON (fallback pour dev local)
        const response = await fetch('products-catalog.json');
        const products = await response.json();
        
        console.log(`📦 ${products.length} produits chargés depuis le catalogue`);
        
        // Enrichir les données avec des informations calculées
        return products.map(product => ({
            ...product,
            // Calculer les filtres automatiquement
            searchTerms: generateSearchTerms(product),
            // Ajouter des métadonnées
            isNew: isNewProduct(product),
            isPopular: product.reviewCount > 200,
            isBestseller: product.badges.includes('bestseller'),
            // Normaliser les URLs
            bolUrl: ensureBolUrl(product.bolUrl, product),
            // Ajouter des informations de livraison
            deliveryInfo: getDeliveryInfo(product)
        }));
        
    } catch (error) {
        console.error('❌ Erreur lors du chargement du catalogue:', error);
        console.log('⚠️ Vérifiez que products-catalog.json existe et est valide');
        return []; // Retourner tableau vide au lieu de fallback
    }
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

// Déterminer si un produit est nouveau (basé sur l'ID ou les badges)
function isNewProduct(product) {
    return product.badges.includes('new') || product.id > 40; // Les derniers produits
}

// S'assurer que l'URL bol.com est correcte
function ensureBolUrl(url, product) {
    if (url && url.includes('bol.com')) {
        return url;
    }
    
    // Générer une URL bol.com générique si manquante
    const slug = `${product.brand}-${product.name}`
        .toLowerCase()
        .replace(/[^a-z0-9\s]/g, '')
        .replace(/\s+/g, '-')
        .substring(0, 50);
    
    return `https://www.bol.com/nl/nl/p/${slug}/9200000087654${product.id.toString().padStart(3, '0')}/`;
}

// Obtenir les informations de livraison
function getDeliveryInfo(product) {
    const info = {
        inStock: product.inStock,
        fastDelivery: product.fastDelivery,
        freeShipping: product.price >= 20,
        deliveryText: ''
    };
    
    if (!product.inStock) {
        info.deliveryText = 'Tijdelijk uitverkocht';
    } else if (product.fastDelivery) {
        info.deliveryText = 'Morgen in huis';
    } else {
        info.deliveryText = '2-3 werkdagen';
    }
    
    return info;
}

// Données de fallback si le catalogue ne peut pas être chargé
function getFallbackProducts() {
    return [
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
            fastDelivery: true,
            searchTerms: "yarrah biologische kip rund trainingssnacks training biologisch natuurlijk graanvrij",
            isNew: false,
            isPopular: false,
            isBestseller: true,
            deliveryInfo: {
                inStock: true,
                fastDelivery: true,
                freeShipping: false,
                deliveryText: 'Morgen in huis'
            }
        }
    ];
}

// Filtrer les produits par catégorie
function filterProductsByCategory(products, category) {
    if (!category || category === 'all') {
        return products;
    }
    
    return products.filter(product => product.category === category);
}

// Rechercher dans les produits
function searchProducts(products, searchTerm) {
    if (!searchTerm || searchTerm.length < 2) {
        return products;
    }
    
    const term = searchTerm.toLowerCase();
    
    return products.filter(product => 
        product.searchTerms.includes(term) ||
        product.name.toLowerCase().includes(term) ||
        product.brand.toLowerCase().includes(term)
    );
}

// Trier les produits
function sortProducts(products, sortBy) {
    const sorted = [...products];
    
    switch (sortBy) {
        case 'price-low':
            return sorted.sort((a, b) => a.price - b.price);
        case 'price-high':
            return sorted.sort((a, b) => b.price - a.price);
        case 'rating':
            return sorted.sort((a, b) => b.rating - a.rating);
        case 'name':
            return sorted.sort((a, b) => a.name.localeCompare(b.name));
        case 'newest':
            return sorted.sort((a, b) => b.id - a.id);
        case 'popular':
        default:
            return sorted.sort((a, b) => {
                // Prioriser bestsellers, puis par nombre de reviews
                if (a.isBestseller && !b.isBestseller) return -1;
                if (!a.isBestseller && b.isBestseller) return 1;
                return b.reviewCount - a.reviewCount;
            });
    }
}

// Obtenir les produits recommandés
function getRecommendedProducts(products, currentProductId = null, limit = 4) {
    let recommended = products
        .filter(p => p.id !== currentProductId)
        .filter(p => p.isBestseller || p.isPopular || p.rating >= 4.5)
        .sort((a, b) => b.rating - a.rating)
        .slice(0, limit);
    
    // Si pas assez de produits recommandés, compléter avec d'autres
    if (recommended.length < limit) {
        const additional = products
            .filter(p => p.id !== currentProductId)
            .filter(p => !recommended.includes(p))
            .sort((a, b) => b.reviewCount - a.reviewCount)
            .slice(0, limit - recommended.length);
        
        recommended = [...recommended, ...additional];
    }
    
    return recommended;
}

// Obtenir les statistiques du catalogue
function getCatalogStats(products) {
    const stats = {
        totalProducts: products.length,
        inStockProducts: products.filter(p => p.inStock).length,
        brands: [...new Set(products.map(p => p.brand))].length,
        categories: [...new Set(products.map(p => p.category))].length,
        averagePrice: products.reduce((sum, p) => sum + p.price, 0) / products.length,
        averageRating: products.reduce((sum, p) => sum + p.rating, 0) / products.length,
        priceRange: {
            min: Math.min(...products.map(p => p.price)),
            max: Math.max(...products.map(p => p.price))
        }
    };
    
    return stats;
}

// Exporter les fonctions
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        loadProductsFromCatalog,
        filterProductsByCategory,
        searchProducts,
        sortProducts,
        getRecommendedProducts,
        getCatalogStats
    };
}
