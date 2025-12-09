/* ========================================
   CATALOG GENERATOR - Génère un catalogue complet
   Basé sur les marques et produits populaires
   ======================================== */

const fs = require('fs');

function generateCompleteCatalog() {
    console.log('🐕 Génération du catalogue complet de hondensnacks...\n');
    
    const catalog = [
        // YARRAH - Biologische snacks
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
            description: "100% biologische trainingssnacks met kip en rund. Perfect voor training en beloning van je hond.",
            category: "training",
            age: ["puppy", "adult"],
            size: ["small", "medium", "large"],
            features: ["biologisch", "natuurlijk", "graanvrij"],
            weight: "200g",
            ingredients: "Biologische kip (40%), biologisch rundvlees (20%), biologische rijst, biologische groenten",
            badges: ["bestseller", "bio"],
            bolUrl: "https://www.bol.com/nl/nl/p/yarrah-biologische-trainingssnacks-kip-rund/9200000087654321/",
            inStock: true,
            fastDelivery: true
        },
        {
            id: 2,
            name: "Yarrah Biologische Vis Trainingssnacks",
            brand: "Yarrah",
            price: 9.45,
            originalPrice: null,
            pricePerUnit: "€4.73 per 100g",
            image: "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400&h=300&fit=crop",
            rating: 4.6,
            reviewCount: 89,
            description: "Biologische trainingssnacks met vis voor honden met een gevoelige maag.",
            category: "training",
            age: ["adult", "senior"],
            size: ["small", "medium"],
            features: ["biologisch", "hypoallergeen", "graanvrij"],
            weight: "200g",
            ingredients: "Biologische vis (45%), biologische aardappel, biologische erwten",
            badges: ["bio", "hypoallergeen"],
            bolUrl: "https://www.bol.com/nl/nl/p/yarrah-biologische-vis-trainingssnacks/9200000087654322/",
            inStock: true,
            fastDelivery: true
        },
        
        // LILY'S KITCHEN - Premium natuurlijke snacks
        {
            id: 3,
            name: "Lily's Kitchen Puppy Training Treats",
            brand: "Lily's Kitchen",
            price: 6.49,
            originalPrice: 7.99,
            pricePerUnit: "€6.49 per 100g",
            image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
            rating: 4.7,
            reviewCount: 234,
            description: "Natuurlijke puppy trainingssnacks met kip en zoete aardappel. Speciaal ontwikkeld voor puppy's.",
            category: "puppy",
            age: ["puppy"],
            size: ["small", "medium"],
            features: ["natuurlijk", "graanvrij", "puppy-formule"],
            weight: "100g",
            ingredients: "Kip (30%), zoete aardappel, erwten, kippenvlees gedroogd",
            badges: ["new", "sale", "puppy"],
            bolUrl: "https://www.bol.com/nl/nl/p/lilys-kitchen-puppy-training-treats/9200000087654323/",
            inStock: true,
            fastDelivery: true
        },
        {
            id: 4,
            name: "Lily's Kitchen Dental Chews Mint & Parsley",
            brand: "Lily's Kitchen",
            price: 12.95,
            originalPrice: null,
            pricePerUnit: "€2.59 per stuk",
            image: "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop",
            rating: 4.5,
            reviewCount: 167,
            description: "Natuurlijke kauwsnacks met munt en peterselie voor frisse adem en gezonde tanden.",
            category: "dental",
            age: ["adult", "senior"],
            size: ["medium", "large"],
            features: ["natuurlijk", "dental-care", "frisse-adem"],
            weight: "5 stuks",
            ingredients: "Kip, munt, peterselie, zoete aardappel, glycerine",
            badges: ["dental"],
            bolUrl: "https://www.bol.com/nl/nl/p/lilys-kitchen-dental-chews-mint-parsley/9200000087654324/",
            inStock: true,
            fastDelivery: false
        },
        
        // GREEN PETFOOD - Duurzame snacks
        {
            id: 5,
            name: "Green Petfood InsectDog Hypoallergeen Snacks",
            brand: "Green Petfood",
            price: 11.95,
            originalPrice: null,
            pricePerUnit: "€5.98 per 100g",
            image: "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400&h=300&fit=crop",
            rating: 4.4,
            reviewCount: 98,
            description: "Innovatieve hypoallergene snacks met insectenproteïne. Duurzaam en gezond voor je hond.",
            category: "hypoallergeen",
            age: ["adult"],
            size: ["small", "medium", "large"],
            features: ["hypoallergeen", "duurzaam", "insecten-proteïne", "graanvrij"],
            weight: "200g",
            ingredients: "Insectenproteïne (40%), aardappel, erwten, lijnzaad",
            badges: ["eco", "hypoallergeen"],
            bolUrl: "https://www.bol.com/nl/nl/p/green-petfood-insectdog-hypoallergeen/9200000087654325/",
            inStock: true,
            fastDelivery: true
        },
        
        // ZUKE'S - Training specialists
        {
            id: 6,
            name: "Zuke's Mini Naturals Zalm Training Treats",
            brand: "Zuke's",
            price: 9.95,
            originalPrice: null,
            pricePerUnit: "€5.85 per 100g",
            image: "https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400&h=300&fit=crop",
            rating: 4.9,
            reviewCount: 312,
            description: "Mini trainingssnacks met echte zalm. Ideaal voor frequente beloningen tijdens training.",
            category: "training",
            age: ["puppy", "adult"],
            size: ["small", "medium"],
            features: ["natuurlijk", "glutenvrij", "mini-formaat"],
            weight: "170g",
            ingredients: "Zalm, aardappel, glycerine, tapioca",
            badges: ["bestseller", "training"],
            bolUrl: "https://www.bol.com/nl/nl/p/zukes-mini-naturals-zalm-training/9200000087654326/",
            inStock: false,
            fastDelivery: false
        },
        {
            id: 7,
            name: "Zuke's Puppy Naturals Kalkoen & Zoete Aardappel",
            brand: "Zuke's",
            price: 8.75,
            originalPrice: null,
            pricePerUnit: "€5.15 per 100g",
            image: "https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=400&h=300&fit=crop",
            rating: 4.7,
            reviewCount: 189,
            description: "Zachte puppy snacks met kalkoen en zoete aardappel. Perfect voor jonge honden.",
            category: "puppy",
            age: ["puppy"],
            size: ["small"],
            features: ["puppy-formule", "zacht", "natuurlijk"],
            weight: "170g",
            ingredients: "Kalkoen, zoete aardappel, erwten, lijnzaad",
            badges: ["puppy", "soft"],
            bolUrl: "https://www.bol.com/nl/nl/p/zukes-puppy-naturals-kalkoen/9200000087654327/",
            inStock: true,
            fastDelivery: true
        },
        
        // WELLNESS - Core series
        {
            id: 8,
            name: "Wellness Core Pure Rewards Kip Freeze-Dried",
            brand: "Wellness",
            price: 14.95,
            originalPrice: 16.95,
            pricePerUnit: "€29.90 per 100g",
            image: "https://images.unsplash.com/photo-1517849845537-4d257902454a?w=400&h=300&fit=crop",
            rating: 4.8,
            reviewCount: 145,
            description: "Premium freeze-dried kip snacks. 100% pure kip, geen toevoegingen.",
            category: "training",
            age: ["adult", "senior"],
            size: ["small", "medium", "large"],
            features: ["freeze-dried", "100%-vlees", "premium"],
            weight: "50g",
            ingredients: "Kip (100%)",
            badges: ["premium", "sale"],
            bolUrl: "https://www.bol.com/nl/nl/p/wellness-core-pure-rewards-kip/9200000087654328/",
            inStock: true,
            fastDelivery: true
        },
        
        // BLUE BUFFALO - Wilderness series
        {
            id: 9,
            name: "Blue Buffalo Wilderness Zalm Bites",
            brand: "Blue Buffalo",
            price: 7.95,
            originalPrice: null,
            pricePerUnit: "€7.95 per 100g",
            image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
            rating: 4.6,
            reviewCount: 203,
            description: "Wilderness zalm bites met echte zalm als eerste ingrediënt. Graanvrij en natuurlijk.",
            category: "training",
            age: ["adult"],
            size: ["medium", "large"],
            features: ["graanvrij", "wilderness", "zalm"],
            weight: "100g",
            ingredients: "Zalm, aardappel, erwten, lijnzaad, blauwe bessen",
            badges: ["wilderness"],
            bolUrl: "https://www.bol.com/nl/nl/p/blue-buffalo-wilderness-zalm-bites/9200000087654329/",
            inStock: true,
            fastDelivery: true
        },
        
        // BENEBONE - Kauwsnacks
        {
            id: 10,
            name: "Benebone Wishbone Bacon Flavor",
            brand: "Benebone",
            price: 16.95,
            originalPrice: null,
            pricePerUnit: "€16.95 per stuk",
            image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
            rating: 4.7,
            reviewCount: 278,
            description: "Duurzame kauwsnack met bacon smaak. Speciaal ontworpen voor krachtige kauwen.",
            category: "kauwsnacks",
            age: ["adult", "senior"],
            size: ["medium", "large"],
            features: ["duurzaam", "bacon-smaak", "krachtig-kauwen"],
            weight: "1 stuk",
            ingredients: "Nylon, bacon aroma",
            badges: ["durable"],
            bolUrl: "https://www.bol.com/nl/nl/p/benebone-wishbone-bacon-flavor/9200000087654330/",
            inStock: true,
            fastDelivery: false
        }
    ];
    
    // Ajouter meer producten voor een vollere catalogus
    const additionalProducts = generateAdditionalProducts(catalog.length);
    const fullCatalog = [...catalog, ...additionalProducts];
    
    // Sauvegarder le catalogue
    const outputFile = 'winkel/products-catalog.json';
    fs.writeFileSync(outputFile, JSON.stringify(fullCatalog, null, 2), 'utf8');
    
    console.log(`✅ Catalogue généré avec succès!`);
    console.log(`📁 Fichier: ${outputFile}`);
    console.log(`🎯 ${fullCatalog.length} produits au total\n`);
    
    // Statistiques
    generateCatalogStats(fullCatalog);
    
    return fullCatalog;
}

function generateAdditionalProducts(startId) {
    const brands = ['Yarrah', "Lily's Kitchen", 'Green Petfood', "Zuke's", 'Wellness', 'Blue Buffalo', 'Benebone', 'Kong', 'Nylabone'];
    const categories = ['training', 'kauwsnacks', 'puppy', 'dental', 'hypoallergeen'];
    const baseNames = [
        'Premium Training Treats',
        'Natural Dental Chews',
        'Puppy Soft Bites',
        'Hypoallergenic Snacks',
        'Freeze-Dried Treats',
        'Grain-Free Bites',
        'Organic Training Rewards',
        'Senior Care Treats',
        'Mini Training Snacks',
        'Large Breed Chews'
    ];
    
    const additionalProducts = [];
    
    for (let i = 0; i < 40; i++) {
        const brand = brands[Math.floor(Math.random() * brands.length)];
        const category = categories[Math.floor(Math.random() * categories.length)];
        const baseName = baseNames[Math.floor(Math.random() * baseNames.length)];
        const price = Math.round((Math.random() * 15 + 5) * 100) / 100;
        const hasDiscount = Math.random() > 0.8;
        
        additionalProducts.push({
            id: startId + i + 1,
            name: `${brand} ${baseName} ${getVariant()}`,
            brand: brand,
            price: price,
            originalPrice: hasDiscount ? Math.round((price * 1.2) * 100) / 100 : null,
            pricePerUnit: `€${(price / 100 * Math.random() * 50 + 50).toFixed(2)} per 100g`,
            image: getRandomImage(),
            rating: Math.round((4.0 + Math.random() * 1.0) * 10) / 10,
            reviewCount: Math.floor(Math.random() * 300) + 20,
            description: generateDescription(brand, category),
            category: category,
            age: getRandomAge(),
            size: getRandomSize(),
            features: getRandomFeatures(),
            weight: getRandomWeight(),
            ingredients: generateIngredients(category),
            badges: generateRandomBadges(i, hasDiscount),
            bolUrl: `https://www.bol.com/nl/nl/p/${brand.toLowerCase().replace(/[^a-z0-9]/g, '-')}-${baseName.toLowerCase().replace(/[^a-z0-9]/g, '-')}/92000000876543${30 + i}/`,
            inStock: Math.random() > 0.1,
            fastDelivery: Math.random() > 0.3
        });
    }
    
    return additionalProducts;
}

function getVariant() {
    const variants = ['Kip', 'Zalm', 'Rund', 'Lam', 'Vis', 'Kalkoen', 'Eend', 'Mix'];
    return variants[Math.floor(Math.random() * variants.length)];
}

function getRandomImage() {
    const images = [
        'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop',
        'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400&h=300&fit=crop',
        'https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop',
        'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop',
        'https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400&h=300&fit=crop',
        'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400&h=300&fit=crop',
        'https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=400&h=300&fit=crop',
        'https://images.unsplash.com/photo-1517849845537-4d257902454a?w=400&h=300&fit=crop'
    ];
    return images[Math.floor(Math.random() * images.length)];
}

function getRandomAge() {
    const options = [
        ['puppy'],
        ['adult'],
        ['senior'],
        ['puppy', 'adult'],
        ['adult', 'senior'],
        ['puppy', 'adult', 'senior']
    ];
    return options[Math.floor(Math.random() * options.length)];
}

function getRandomSize() {
    const options = [
        ['small'],
        ['medium'],
        ['large'],
        ['small', 'medium'],
        ['medium', 'large'],
        ['small', 'medium', 'large']
    ];
    return options[Math.floor(Math.random() * options.length)];
}

function getRandomFeatures() {
    const allFeatures = ['biologisch', 'natuurlijk', 'graanvrij', 'glutenvrij', 'hypoallergeen', 'duurzaam'];
    const count = Math.floor(Math.random() * 3) + 1;
    const shuffled = allFeatures.sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}

function getRandomWeight() {
    const weights = ['50g', '100g', '150g', '200g', '250g', '300g', '500g', '1 stuk', '3 stuks', '5 stuks'];
    return weights[Math.floor(Math.random() * weights.length)];
}

function generateDescription(brand, category) {
    const descriptions = {
        training: `Hoogwaardige trainingssnacks van ${brand}. Perfect voor training en beloning.`,
        kauwsnacks: `Duurzame kauwsnacks van ${brand} voor gezonde tanden en langdurig kauwplezier.`,
        puppy: `Speciaal ontwikkelde puppy snacks van ${brand} voor jonge honden.`,
        dental: `Dental care snacks van ${brand} voor gezonde tanden en frisse adem.`,
        hypoallergeen: `Hypoallergene snacks van ${brand} voor honden met voedselgevoeligheden.`
    };
    return descriptions[category] || `Premium hondensnacks van ${brand}.`;
}

function generateIngredients(category) {
    const ingredients = {
        training: 'Kip, rijst, groenten, vitaminen',
        kauwsnacks: 'Runderhuid, glycerine, natuurlijke aroma\'s',
        puppy: 'Kip, zoete aardappel, erwten, lijnzaad',
        dental: 'Kip, munt, peterselie, calcium',
        hypoallergeen: 'Eend, aardappel, erwten, lijnzaad'
    };
    return ingredients[category] || 'Natuurlijke ingrediënten';
}

function generateRandomBadges(index, hasDiscount) {
    const badges = [];
    
    if (index < 3) badges.push('bestseller');
    if (Math.random() > 0.9) badges.push('new');
    if (Math.random() > 0.7) badges.push('bio');
    if (hasDiscount) badges.push('sale');
    
    return badges;
}

function generateCatalogStats(products) {
    console.log('📊 STATISTIQUES DU CATALOGUE:');
    console.log('─'.repeat(50));
    
    const brands = [...new Set(products.map(p => p.brand))];
    console.log(`🏭 Marques: ${brands.length}`);
    console.log(`   ${brands.join(', ')}`);
    
    const categories = [...new Set(products.map(p => p.category))];
    console.log(`\n🏷️  Catégories: ${categories.length}`);
    categories.forEach(cat => {
        const count = products.filter(p => p.category === cat).length;
        console.log(`   • ${cat}: ${count} produits`);
    });
    
    const prices = products.map(p => p.price).filter(p => p > 0);
    const avgPrice = (prices.reduce((a, b) => a + b, 0) / prices.length).toFixed(2);
    console.log(`\n💰 Prix: €${Math.min(...prices).toFixed(2)} - €${Math.max(...prices).toFixed(2)}`);
    console.log(`   Moyenne: €${avgPrice}`);
    
    const inStock = products.filter(p => p.inStock).length;
    console.log(`\n📦 En stock: ${inStock}/${products.length} (${Math.round(inStock/products.length*100)}%)`);
    
    console.log('─'.repeat(50));
}

// Exécuter la génération
if (require.main === module) {
    generateCompleteCatalog();
}

module.exports = { generateCompleteCatalog };
