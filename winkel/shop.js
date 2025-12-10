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
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
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
        price: 19.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
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
        id: 6,
        name: "HobbyFirst Canex Trainers Konijn",
        brand: "Hobbyfirst",
        category: "training",
        price: 18.0,
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
        id: 7,
        name: "Softies Eend",
        brand: "Bellobox",
        category: "natuurlijk",
        price: 8.5,
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
    },
    {
        id: 8,
        name: "BROK Verjaardag Snackpakket",
        brand: "BROK shop",
        category: "natuurlijk",
        price: 25.0,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "BROK Verjaardag Snackpakket van BROK shop. Runder, Buffelhuid mix",
        weight: "300 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/brok-verjaardag-snackpakket.html"
    },
    {
        id: 9,
        name: "Petstyle Living Sticks Kip 100 stuks",
        brand: "Petstyle Living",
        category: "natuurlijk",
        price: 25.95,
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        description: "Petstyle Living Sticks Kip 100 stuks van Petstyle Living. Best-seller (969 reviews)",
        weight: "n.b.",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-sticks-kip-100-stuks.html"
    },
    {
        id: 10,
        name: "Petstyle Living Sticks Eend 100 stuks",
        brand: "Petstyle Living",
        category: "natuurlijk",
        price: 25.95,
        image: "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop",
        description: "Petstyle Living Sticks Eend 100 stuks van Petstyle Living. Populair (969 reviews)",
        weight: "n.b.",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-sticks-eend-100-stuks.html"
    },
    {
        id: 11,
        name: "Petstyle Living Sticks Kip & Rund 100 stuks",
        brand: "Petstyle Living",
        category: "natuurlijk",
        price: 25.95,
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        description: "Petstyle Living Sticks Kip & Rund 100 stuks van Petstyle Living. Mixed (969 reviews)",
        weight: "n.b.",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
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
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        description: "Petstyle Living Kipfilet van Petstyle Living. Puur kipfilet",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-kipfilet.html"
    },
    {
        id: 13,
        name: "Petstyle Living Kauwstaven Kip",
        brand: "Petstyle Living",
        category: "kauwsnacks",
        price: 29.95,
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        description: "Petstyle Living Kauwstaven Kip van Petstyle Living. 20cm lang",
        weight: "n.b.",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-kauwstaven-kip.html"
    },
    {
        id: 14,
        name: "Petstyle Living Kauwring Kip",
        brand: "Petstyle Living",
        category: "kauwsnacks",
        price: 32.95,
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        description: "Petstyle Living Kauwring Kip van Petstyle Living. 7,5cm, 91 reviews",
        weight: "n.b.",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petstyle-living-kauwring-kip.html"
    },
    {
        id: 15,
        name: "Runderbot XL 5 stuks",
        brand: "Merkloos/Oswalt",
        category: "natuurlijk",
        price: 16.49,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Runderbot XL 5 stuks van Merkloos/Oswalt. 100% natuurlijk",
        weight: "n.b.",
        age: ["adult"],
        size: ["groot"],
        features: ["natuurlijk"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/runderbot-xl-5-stuks.html"
    },
    {
        id: 16,
        name: "Konijnenoren 1kg",
        brand: "Pawty/Oswalt",
        category: "natuurlijk",
        price: 17.49,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Konijnenoren 1kg van Pawty/Oswalt. Met haar, top kwaliteit",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/konijnenoren-1kg.html"
    },
    {
        id: 17,
        name: "Konijnenoren 2x1kg Duo",
        brand: "Merkloos/Oswalt",
        category: "natuurlijk",
        price: 26.49,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Konijnenoren 2x1kg Duo van Merkloos/Oswalt. Double pack",
        weight: "2000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/konijnenoren-2x1kg-duo.html"
    },
    {
        id: 18,
        name: "Anti Poep Eten DogSuppy",
        brand: "DogSuppy.be",
        category: "supplementen",
        price: 28.4,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Anti Poep Eten DogSuppy van DogSuppy.be. Coprophagia, digestie & adem",
        weight: "237 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["supplement"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/anti-poep-eten-dogsuppy.html"
    },
    {
        id: 19,
        name: "Trainers Runderlong 1kg",
        brand: "lutopets",
        category: "training",
        price: 24.9,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Trainers Runderlong 1kg van lutopets. Hypoallergeen, luchtig",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["hypoallergeen"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/trainers-runderlong-1kg.html"
    },
    {
        id: 20,
        name: "Gedroogde Kippenpoten 1kg",
        brand: "123diepvriesvoer.nl",
        category: "natuurlijk",
        price: 14.99,
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        description: "Gedroogde Kippenpoten 1kg van 123diepvriesvoer.nl. 100% natuurlijk, glutenvrij",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk", "glutenvrij"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/gedroogde-kippenpoten-1kg.html"
    },
    {
        id: 21,
        name: "Animalking Runderhart 2kg",
        brand: "Animal King",
        category: "natuurlijk",
        price: 39.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Animalking Runderhart 2kg van Animal King. Voor training/beloning",
        weight: "2000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/animalking-runderhart-2kg.html"
    },
    {
        id: 22,
        name: "BROK Stevige Kauwers 2kg",
        brand: "BROK shop",
        category: "kauwsnacks",
        price: 35.0,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "BROK Stevige Kauwers 2kg van BROK shop. Voor sterke kauwers",
        weight: "2000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/brok-stevige-kauwers-2kg.html"
    },
    {
        id: 23,
        name: "Gedroogde Longen 6x1kg",
        brand: "Merkloos/Oswalt",
        category: "natuurlijk",
        price: 44.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Gedroogde Longen 6x1kg van Merkloos/Oswalt. Zeer verteerbaar",
        weight: "6000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/gedroogde-longen-6x1kg.html"
    },
    {
        id: 24,
        name: "Pawty Snackbox Mix",
        brand: "Pawty BE",
        category: "natuurlijk",
        price: 29.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Pawty Snackbox Mix van Pawty BE. Diverse natuurlijke snacks",
        weight: "2000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/pawty-snackbox-mix.html"
    },
    {
        id: 25,
        name: "Hertengewei XXL (400-450g)",
        brand: "Topdiervoeding.nl",
        category: "natuurlijk",
        price: 48.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Hertengewei XXL (400-450g) van Topdiervoeding.nl. Zeer lang kauwplezier",
        weight: "400 g",
        age: ["alle leeftijden"],
        size: ["groot"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/hertengewei-xxl-400-450g.html"
    },
    {
        id: 26,
        name: "Hertengewei L (200-250g)",
        brand: "Topdiervoeding.nl",
        category: "natuurlijk",
        price: 27.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Hertengewei L (200-250g) van Topdiervoeding.nl. Medium large",
        weight: "250 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/hertengewei-l-200-250g.html"
    },
    {
        id: 27,
        name: "Hertengewei M (150-180g)",
        brand: "Topdiervoeding.nl",
        category: "natuurlijk",
        price: 23.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Hertengewei M (150-180g) van Topdiervoeding.nl. Medium maat",
        weight: "180 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/hertengewei-m-150-180g.html"
    },
    {
        id: 28,
        name: "Hertengewei XXL (360-400g)",
        brand: "Topdiervoeding.nl",
        category: "natuurlijk",
        price: 42.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Hertengewei XXL (360-400g) van Topdiervoeding.nl. Extra large kauwbot",
        weight: "400 g",
        age: ["alle leeftijden"],
        size: ["groot"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/hertengewei-xxl-360-400g.html"
    },
    {
        id: 29,
        name: "Imby Multipack 9x100gr",
        brand: "Imby",
        category: "natuurlijk",
        price: 29.7,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Imby Multipack 9x100gr van Imby. Vet/Dental/Bedtime mix",
        weight: "900 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/imby-multipack-9x100gr.html"
    },
    {
        id: 30,
        name: "Imby Skin & Coat 5x100gr",
        brand: "Imby",
        category: "natuurlijk",
        price: 24.75,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Imby Skin & Coat 5x100gr van Imby. Insect-based, laag calorie",
        weight: "500 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/imby-skin-coat-5x100gr.html"
    },
    {
        id: 31,
        name: "Runderspaghetti 200g",
        brand: "Lifetime Petfood",
        category: "natuurlijk",
        price: 14.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Runderspaghetti 200g van Lifetime Petfood. Hypoallergeen, gedroogd",
        weight: "200 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["hypoallergeen", "gedroogd"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/runderspaghetti-200g.html"
    },
    {
        id: 32,
        name: "Rundvleestrainers 400g",
        brand: "Lifetime Petfood",
        category: "training",
        price: 19.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Rundvleestrainers 400g van Lifetime Petfood. Trainingssnack",
        weight: "400 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/rundvleestrainers-400g.html"
    },
    {
        id: 33,
        name: "Runderkophuid 15cm 200g",
        brand: "Lifetime Petfood",
        category: "natuurlijk",
        price: 11.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Runderkophuid 15cm 200g van Lifetime Petfood. Hypoallergeen",
        weight: "215 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["hypoallergeen"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/runderkophuid-15cm-200g.html"
    },
    {
        id: 34,
        name: "Hondenbot Olijfhout L",
        brand: "Kivo Petfood",
        category: "natuurlijk",
        price: 14.5,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Hondenbot Olijfhout L van Kivo Petfood. Splitst niet",
        weight: "400 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/hondenbot-olijfhout-l.html"
    },
    {
        id: 35,
        name: "Kivo Petfood Spiering 200g",
        brand: "Kivo Petfood",
        category: "natuurlijk",
        price: 12.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Kivo Petfood Spiering 200g van Kivo Petfood. 100% spiering",
        weight: "200 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/kivo-petfood-spiering-200g.html"
    },
    {
        id: 36,
        name: "Pensstaafjes Rund 1000g",
        brand: "Merkloos/Oswalt",
        category: "natuurlijk",
        price: 22.49,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Pensstaafjes Rund 1000g van Merkloos/Oswalt. Runderpens staafjes",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/pensstaafjes-rund-1000g.html"
    },
    {
        id: 37,
        name: "Yak Kaas YAKBOT S 5 stuks",
        brand: "Merkloos/Topmast",
        category: "natuurlijk",
        price: 22.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Yak Kaas YAKBOT S 5 stuks van Merkloos/Topmast. 60-70g per stuk",
        weight: "60 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/yak-kaas-yakbot-s-5-stuks.html"
    },
    {
        id: 38,
        name: "Yak Kaas YAKBOT M 5 stuks",
        brand: "Merkloos/Topmast",
        category: "natuurlijk",
        price: 23.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Yak Kaas YAKBOT M 5 stuks van Merkloos/Topmast. Best-seller (34 reviews)",
        weight: "85 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/yak-kaas-yakbot-m-5-stuks.html"
    },
    {
        id: 39,
        name: "Yak Kaas YAKBOT L 3 stuks",
        brand: "Merkloos/Topmast",
        category: "natuurlijk",
        price: 25.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Yak Kaas YAKBOT L 3 stuks van Merkloos/Topmast. 90-100g per stuk",
        weight: "110 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/yak-kaas-yakbot-l-3-stuks.html"
    },
    {
        id: 40,
        name: "Yak Kaas YAKBOT XL 2 stuks",
        brand: "Merkloos/Topmast",
        category: "natuurlijk",
        price: 20.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Yak Kaas YAKBOT XL 2 stuks van Merkloos/Topmast. 115-125g per stuk",
        weight: "110 g",
        age: ["alle leeftijden"],
        size: ["groot"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/yak-kaas-yakbot-xl-2-stuks.html"
    },
    {
        id: 41,
        name: "Yak Kaas 120-140g",
        brand: "Merkloos",
        category: "natuurlijk",
        price: 12.49,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Yak Kaas 120-140g van Merkloos. Origineel Himalaya",
        weight: "120 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/yak-kaas-120-140g.html"
    },
    {
        id: 42,
        name: "Qwisple Lamskophuid 1kg",
        brand: "Qwisple",
        category: "natuurlijk",
        price: 18.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Qwisple Lamskophuid 1kg van Qwisple. Gedroogd, natuurlijk",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk", "gedroogd"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/qwisple-lamskophuid-1kg.html"
    },
    {
        id: 43,
        name: "Qwisple Geitenoren 1kg",
        brand: "Qwisple",
        category: "natuurlijk",
        price: 29.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Qwisple Geitenoren 1kg van Qwisple. Gedroogd, natuurlijk",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk", "gedroogd"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/qwisple-geitenoren-1kg.html"
    },
    {
        id: 44,
        name: "Longen Gerookt 1kg",
        brand: "Merkloos/Oswalt",
        category: "natuurlijk",
        price: 12.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Longen Gerookt 1kg van Merkloos/Oswalt. Gerookt, 100% rund",
        weight: "1000 g",
        age: ["adult"],
        size: ["alle maten"],
        features: ["natuurlijk"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/longen-gerookt-1kg.html"
    },
    {
        id: 45,
        name: "Runderluchtpijp 20 stuks",
        brand: "Topdiervoeding.nl",
        category: "natuurlijk",
        price: 39.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Runderluchtpijp 20 stuks van Topdiervoeding.nl. 30cm lang, reinigt tanden",
        weight: "3000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/runderluchtpijp-20-stuks.html"
    },
    {
        id: 46,
        name: "Varkensoren Chips 1kg",
        brand: "Boomy",
        category: "natuurlijk",
        price: 22.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Varkensoren Chips 1kg van Boomy. Krokant, 6-7cm stukjes",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/varkensoren-chips-1kg.html"
    },
    {
        id: 47,
        name: "Varkens Neuzen 25 stuks",
        brand: "snackmeester",
        category: "natuurlijk",
        price: 21.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Varkens Neuzen 25 stuks van snackmeester. Sterke kauw, laag vet",
        weight: "n.b.",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/varkens-neuzen-25-stuks.html"
    },
    {
        id: 48,
        name: "Konijn Oren 1kg - snackmeester",
        brand: "snackmeester",
        category: "natuurlijk",
        price: 16.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Konijn Oren 1kg - snackmeester van snackmeester. Hypoallergeen",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["hypoallergeen"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/konijn-oren-1kg-snackmeester.html"
    },
    {
        id: 49,
        name: "Konijn Oren 1kg - snackmeester",
        brand: "snackmeester",
        category: "natuurlijk",
        price: 23.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Konijn Oren 1kg - snackmeester van snackmeester. Extra kwaliteit",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/konijn-oren-1kg-snackmeester.html"
    },
    {
        id: 50,
        name: "Advanced Chew Dental Sticks",
        brand: "DogSuppy.be",
        category: "dental",
        price: 23.4,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Advanced Chew Dental Sticks van DogSuppy.be. Zalm, tandenhygiëne",
        weight: "480 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/advanced-chew-dental-sticks.html"
    },
    {
        id: 51,
        name: "Puppy Bellobox - Zonder speelgoed",
        brand: "Bellobox B.V.",
        category: "puppy",
        price: 39.94,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Puppy Bellobox - Zonder speelgoed van Bellobox B.V.. Speciaal voor puppy's",
        weight: "n.b.",
        age: ["puppy"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/puppy-bellobox-zonder-speelgoed.html"
    },
    {
        id: 52,
        name: "Puppy Bellobox - Met speelgoed",
        brand: "Bellobox B.V.",
        category: "puppy",
        price: 39.94,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Puppy Bellobox - Met speelgoed van Bellobox B.V.. Inclusief speelgoed",
        weight: "n.b.",
        age: ["puppy"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/puppy-bellobox-met-speelgoed.html"
    },
    {
        id: 53,
        name: "Hondensnack pakket mix",
        brand: "Versvleeshonden.nl",
        category: "natuurlijk",
        price: 19.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Hondensnack pakket mix van Versvleeshonden.nl. Kennismaakpakket",
        weight: "450 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/hondensnack-pakket-mix.html"
    },
    {
        id: 54,
        name: "Take & Break Mixdoos 48 stuks",
        brand: "Versvleeshonden.nl",
        category: "natuurlijk",
        price: 31.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Take & Break Mixdoos 48 stuks van Versvleeshonden.nl. 4 verschillende smaken",
        weight: "3200 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/take-break-mixdoos-48-stuks.html"
    },
    {
        id: 55,
        name: "Take & Break Pens 50 stuks",
        brand: "Versvleeshonden.nl",
        category: "natuurlijk",
        price: 31.5,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Take & Break Pens 50 stuks van Versvleeshonden.nl. Hypoallergeen, glutenvrij",
        weight: "3200 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["hypoallergeen", "glutenvrij"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/take-break-pens-50-stuks.html"
    },
    {
        id: 56,
        name: "Runderkophuid Topmast 2x1kg",
        brand: "Topmast",
        category: "natuurlijk",
        price: 21.49,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Runderkophuid Topmast 2x1kg van Topmast. 12-15cm lang",
        weight: "2000 g",
        age: ["adult"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/runderkophuid-topmast-2x1kg.html"
    },
    {
        id: 57,
        name: "Kipfilet Topdiervoeding 1kg",
        brand: "Topdiervoeding.nl",
        category: "natuurlijk",
        price: 26.99,
        image: "https://images.unsplash.com/photo-1605568427561-40dd23c2acea?w=400&h=300&fit=crop",
        description: "Kipfilet Topdiervoeding 1kg van Topdiervoeding.nl. 100% kip, gedroogd",
        weight: "1000 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk", "gedroogd"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/kipfilet-topdiervoeding-1kg.html"
    },
    {
        id: 58,
        name: "Petsnack Runderkophuid Platen 5kg",
        brand: "Petsnack/Oswalt",
        category: "natuurlijk",
        price: 39.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Petsnack Runderkophuid Platen 5kg van Petsnack/Oswalt. Grote kauwervaringen",
        weight: "5010 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/petsnack-runderkophuid-platen-5kg.html"
    },
    {
        id: 59,
        name: "Kauwstaaf Runderhuid 13cm 50 stuks",
        brand: "123diepvriesvoer.nl",
        category: "kauwsnacks",
        price: 34.99,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Kauwstaaf Runderhuid 13cm 50 stuks van 123diepvriesvoer.nl. Tanden tandenborstel",
        weight: "1400 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/kauwstaaf-runderhuid-13cm-50-stuks.html"
    },
    {
        id: 60,
        name: "Runder Kauwbot 15cm",
        brand: "Trimmi",
        category: "kauwsnacks",
        price: 6.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Runder Kauwbot 15cm van Trimmi. 100% rund, lekker & gezond",
        weight: "100 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["natuurlijk"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/runder-kauwbot-15cm.html"
    },
    {
        id: 61,
        name: "Soft Bones Glutenvrij 500g",
        brand: "Trimmi",
        category: "natuurlijk",
        price: 11.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Soft Bones Glutenvrij 500g van Trimmi. Zachte, glutenvrije beloning",
        weight: "500 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["glutenvrij"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/soft-bones-glutenvrij-500g.html"
    },
    {
        id: 62,
        name: "Flamingo Buffelhoorn L 400g",
        brand: "Flamingo",
        category: "natuurlijk",
        price: 10.71,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Flamingo Buffelhoorn L 400g van Flamingo. Stevige, langdurig",
        weight: "410 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/flamingo-buffelhoorn-l-400g.html"
    },
    {
        id: 63,
        name: "Boomy Mini Been 2 stuks",
        brand: "Boomy",
        category: "natuurlijk",
        price: 14.3,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Boomy Mini Been 2 stuks van Boomy. 20-25cm, langdurig",
        weight: "400 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/boomy-mini-been-2-stuks.html"
    },
    {
        id: 64,
        name: "Boomy Gevulde Hoefjes 3 stuks",
        brand: "Boomy",
        category: "natuurlijk",
        price: 15.7,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Boomy Gevulde Hoefjes 3 stuks van Boomy. Stevige kauwsnack",
        weight: "600 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/boomy-gevulde-hoefjes-3-stuks.html"
    },
    {
        id: 65,
        name: "Boomy Paardensticks 200g",
        brand: "Boomy",
        category: "natuurlijk",
        price: 18.6,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Boomy Paardensticks 200g van Boomy. Heel hard, voor sterke kauwen",
        weight: "200 g",
        age: ["adult"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/boomy-paardensticks-200g.html"
    },
    {
        id: 66,
        name: "Allerguard anti-allergie 180 stuks",
        brand: "Sharon B",
        category: "supplementen",
        price: 35.95,
        image: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400&h=300&fit=crop",
        description: "Allerguard anti-allergie 180 stuks van Sharon B. Tegen jeuk en allergie",
        weight: "500 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["supplement"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/allerguard-anti-allergie-180-stuks.html"
    },
    {
        id: 67,
        name: "Rosewood Grillers Eend 10x100g",
        brand: "Rosewood",
        category: "natuurlijk",
        price: 26.9,
        image: "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=300&fit=crop",
        description: "Rosewood Grillers Eend 10x100g van Rosewood. 58% eendenvlees",
        weight: "1293 g",
        age: ["alle leeftijden"],
        size: ["alle maten"],
        features: ["premium"],
        inStock: true,
        rating: 4.5,
        reviews: 25,
        url: "../produits/rosewood-grillers-eend-10x100g.html"
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

// Products are already defined above in allProducts array

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
    // Initialize with real products (already defined above)
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
