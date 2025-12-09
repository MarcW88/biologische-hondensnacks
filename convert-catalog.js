/* ========================================
   CATALOG CONVERTER - Excel to JSON
   Convertit le catalogue Excel en données JSON
   ======================================== */

const XLSX = require('xlsx');
const fs = require('fs');
const path = require('path');

// Configuration
const EXCEL_FILE = 'Hondensnacks Catalogus (1).xlsx';
const OUTPUT_FILE = 'winkel/products-catalog.json';

function convertExcelToJSON() {
    console.log('🔄 Conversion du catalogue Excel vers JSON...\n');
    
    try {
        // Lire le fichier Excel
        const workbook = XLSX.readFile(EXCEL_FILE);
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        
        // Convertir en JSON
        const rawData = XLSX.utils.sheet_to_json(worksheet);
        
        console.log(`📊 ${rawData.length} produits trouvés dans le catalogue\n`);
        
        // Transformer les données en format utilisable
        const products = rawData.map((row, index) => {
            return {
                id: index + 1,
                name: cleanString(row['Productnaam'] || row['Product'] || row['Naam'] || ''),
                brand: cleanString(row['Merk'] || row['Brand'] || ''),
                price: parsePrice(row['Prijs'] || row['Price'] || 0),
                originalPrice: parsePrice(row['Oude Prijs'] || row['Original Price'] || null),
                pricePerUnit: cleanString(row['Prijs per eenheid'] || row['Price per unit'] || ''),
                description: cleanString(row['Beschrijving'] || row['Description'] || ''),
                category: mapCategory(row['Categorie'] || row['Category'] || ''),
                age: mapAge(row['Leeftijd'] || row['Age'] || ''),
                size: mapSize(row['Grootte'] || row['Size'] || ''),
                features: mapFeatures(row['Eigenschappen'] || row['Features'] || ''),
                weight: cleanString(row['Gewicht'] || row['Weight'] || ''),
                ingredients: cleanString(row['Ingrediënten'] || row['Ingredients'] || ''),
                bolUrl: cleanString(row['Bol.com URL'] || row['URL'] || ''),
                image: generateImageUrl(row['Afbeelding'] || row['Image'] || ''),
                rating: parseFloat(row['Rating'] || row['Beoordeling'] || (4.0 + Math.random() * 1.0)),
                reviewCount: parseInt(row['Reviews'] || row['Aantal reviews'] || Math.floor(Math.random() * 300) + 50),
                inStock: parseBool(row['Op voorraad'] || row['In Stock'] || true),
                fastDelivery: parseBool(row['Snelle levering'] || row['Fast Delivery'] || true),
                badges: generateBadges(index, row)
            };
        }).filter(product => product.name && product.brand); // Filter empty products
        
        // Sauvegarder en JSON
        fs.writeFileSync(OUTPUT_FILE, JSON.stringify(products, null, 2), 'utf8');
        
        console.log(`✅ Catalogue converti avec succès!`);
        console.log(`📁 Fichier sauvegardé: ${OUTPUT_FILE}`);
        console.log(`🎯 ${products.length} produits traités\n`);
        
        // Générer des statistiques
        generateStats(products);
        
        return products;
        
    } catch (error) {
        console.error('❌ Erreur lors de la conversion:', error.message);
        
        // Générer des données de démonstration si le fichier Excel n'existe pas
        console.log('📝 Génération de données de démonstration...\n');
        return generateDemoData();
    }
}

function cleanString(str) {
    if (!str) return '';
    return str.toString().trim();
}

function parsePrice(price) {
    if (!price) return 0;
    const numStr = price.toString().replace(/[€$,]/g, '').replace(',', '.');
    return parseFloat(numStr) || 0;
}

function parseBool(value) {
    if (typeof value === 'boolean') return value;
    if (typeof value === 'string') {
        return ['ja', 'yes', 'true', '1', 'oui'].includes(value.toLowerCase());
    }
    return Boolean(value);
}

function mapCategory(category) {
    const categoryMap = {
        'training': 'training',
        'trainingssnacks': 'training',
        'kauw': 'kauwsnacks',
        'kauwsnacks': 'kauwsnacks',
        'puppy': 'puppy',
        'pup': 'puppy',
        'dental': 'dental',
        'tandverzorging': 'dental',
        'hypoallergeen': 'hypoallergeen',
        'allergie': 'hypoallergeen'
    };
    
    const cat = category.toLowerCase();
    for (const [key, value] of Object.entries(categoryMap)) {
        if (cat.includes(key)) return value;
    }
    return 'training'; // default
}

function mapAge(age) {
    const ages = [];
    const ageStr = age.toLowerCase();
    
    if (ageStr.includes('puppy') || ageStr.includes('pup') || ageStr.includes('jong')) {
        ages.push('puppy');
    }
    if (ageStr.includes('adult') || ageStr.includes('volwassen') || ageStr.includes('alle')) {
        ages.push('adult');
    }
    if (ageStr.includes('senior') || ageStr.includes('oud')) {
        ages.push('senior');
    }
    
    return ages.length > 0 ? ages : ['adult'];
}

function mapSize(size) {
    const sizes = [];
    const sizeStr = size.toLowerCase();
    
    if (sizeStr.includes('klein') || sizeStr.includes('small') || sizeStr.includes('mini')) {
        sizes.push('small');
    }
    if (sizeStr.includes('middel') || sizeStr.includes('medium') || sizeStr.includes('alle')) {
        sizes.push('medium');
    }
    if (sizeStr.includes('groot') || sizeStr.includes('large') || sizeStr.includes('xl')) {
        sizes.push('large');
    }
    
    return sizes.length > 0 ? sizes : ['medium'];
}

function mapFeatures(features) {
    const featureList = [];
    const featStr = features.toLowerCase();
    
    if (featStr.includes('bio') || featStr.includes('organic')) {
        featureList.push('biologisch');
    }
    if (featStr.includes('natuurlijk') || featStr.includes('natural')) {
        featureList.push('natuurlijk');
    }
    if (featStr.includes('graanvrij') || featStr.includes('grain-free')) {
        featureList.push('graanvrij');
    }
    if (featStr.includes('glutenvrij') || featStr.includes('gluten-free')) {
        featureList.push('glutenvrij');
    }
    if (featStr.includes('duurzaam') || featStr.includes('sustainable')) {
        featureList.push('duurzaam');
    }
    
    return featureList.length > 0 ? featureList : ['natuurlijk'];
}

function generateImageUrl(imagePath) {
    if (imagePath && imagePath.startsWith('http')) {
        return imagePath;
    }
    
    // Générer une image Unsplash aléatoire liée aux chiens/snacks
    const imageIds = [
        'photo-1583337130417-3346a1be7dee', // dog treats
        'photo-1601758228041-f3b2795255f1', // puppy treats
        'photo-1605568427561-40dd23c2acea', // dental sticks
        'photo-1548199973-03cce0bbc87b', // training treats
        'photo-1574158622682-e40e69881006', // dog food
        'photo-1587300003388-59208cc962cb', // healthy treats
        'photo-1592194996308-7b43878e84a6', // natural snacks
        'photo-1517849845537-4d257902454a' // happy dog
    ];
    
    const randomId = imageIds[Math.floor(Math.random() * imageIds.length)];
    return `https://images.unsplash.com/${randomId}?w=400&h=300&fit=crop`;
}

function generateBadges(index, row) {
    const badges = [];
    
    // Bestseller pour les premiers produits
    if (index < 5) badges.push('bestseller');
    
    // New pour certains produits
    if (Math.random() > 0.8) badges.push('new');
    
    // Bio si mentionné
    if (row['Eigenschappen'] && row['Eigenschappen'].toLowerCase().includes('bio')) {
        badges.push('bio');
    }
    
    // Sale si prix réduit
    if (row['Oude Prijs'] && parsePrice(row['Oude Prijs']) > parsePrice(row['Prijs'])) {
        badges.push('sale');
    }
    
    return badges;
}

function generateStats(products) {
    console.log('📊 STATISTIQUES DU CATALOGUE:');
    console.log('─'.repeat(40));
    
    // Marques
    const brands = [...new Set(products.map(p => p.brand))];
    console.log(`🏭 Marques: ${brands.length} (${brands.join(', ')})`);
    
    // Catégories
    const categories = [...new Set(products.map(p => p.category))];
    console.log(`🏷️  Catégories: ${categories.length} (${categories.join(', ')})`);
    
    // Prix
    const prices = products.map(p => p.price).filter(p => p > 0);
    const avgPrice = (prices.reduce((a, b) => a + b, 0) / prices.length).toFixed(2);
    const minPrice = Math.min(...prices).toFixed(2);
    const maxPrice = Math.max(...prices).toFixed(2);
    console.log(`💰 Prix: €${minPrice} - €${maxPrice} (moyenne: €${avgPrice})`);
    
    // Stock
    const inStock = products.filter(p => p.inStock).length;
    console.log(`📦 En stock: ${inStock}/${products.length} (${Math.round(inStock/products.length*100)}%)`);
    
    console.log('─'.repeat(40));
}

function generateDemoData() {
    console.log('📝 Génération de 20 produits de démonstration...\n');
    
    const demoBrands = ['Yarrah', "Lily's Kitchen", 'Green Petfood', "Zuke's", 'Wellness', 'Blue Buffalo'];
    const demoCategories = ['training', 'kauwsnacks', 'puppy', 'dental'];
    const demoProducts = [];
    
    for (let i = 1; i <= 20; i++) {
        const brand = demoBrands[Math.floor(Math.random() * demoBrands.length)];
        const category = demoCategories[Math.floor(Math.random() * demoCategories.length)];
        
        demoProducts.push({
            id: i,
            name: `${brand} ${getCategoryName(category)} Snacks ${i}`,
            brand: brand,
            price: Math.round((Math.random() * 20 + 5) * 100) / 100,
            originalPrice: Math.random() > 0.7 ? Math.round((Math.random() * 5 + 15) * 100) / 100 : null,
            pricePerUnit: `€${(Math.random() * 10 + 2).toFixed(2)} per 100g`,
            description: `Natuurlijke ${category} snacks van ${brand}. Perfect voor dagelijks gebruik.`,
            category: category,
            age: ['adult'],
            size: ['medium'],
            features: ['natuurlijk', 'biologisch'],
            weight: '200g',
            ingredients: 'Kip, rijst, groenten',
            bolUrl: `https://www.bol.com/nl/p/demo-product-${i}/`,
            image: generateImageUrl(''),
            rating: Math.round((4.0 + Math.random() * 1.0) * 10) / 10,
            reviewCount: Math.floor(Math.random() * 300) + 50,
            inStock: Math.random() > 0.1,
            fastDelivery: Math.random() > 0.3,
            badges: i <= 3 ? ['bestseller'] : []
        });
    }
    
    // Sauvegarder les données de démo
    fs.writeFileSync(OUTPUT_FILE, JSON.stringify(demoProducts, null, 2), 'utf8');
    
    console.log(`✅ ${demoProducts.length} produits de démonstration générés`);
    console.log(`📁 Fichier sauvegardé: ${OUTPUT_FILE}\n`);
    
    return demoProducts;
}

function getCategoryName(category) {
    const names = {
        'training': 'Training',
        'kauwsnacks': 'Kauw',
        'puppy': 'Puppy',
        'dental': 'Dental'
    };
    return names[category] || 'Premium';
}

// Exécuter la conversion
if (require.main === module) {
    convertExcelToJSON();
}

module.exports = { convertExcelToJSON };
