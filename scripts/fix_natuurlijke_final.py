#!/usr/bin/env python3
"""
Final fixes for natuurlijke-hondensnacks page
"""

import re

input_file = '/Users/marc/Desktop/biologische-hondensnacks/natuurlijke-hondensnacks/index.html'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Backup
with open(input_file + '.final_backup', 'w', encoding='utf-8') as f:
    f.write(content)

print("🔧 FINAL FIXES")
print("=" * 60)

# 1. Corriger les duplications "Bekijk Bekijk"
content = re.sub(r'Bekijk\s+Bekijk', 'Bekijk', content, flags=re.I)
print("✅ Duplications 'Bekijk Bekijk' corrigées")

# 2. Changer les fonctions showAllProducts et hideAllProducts pour rediriger vers /winkel/
old_show_function = "function showAllProducts() { document.getElementById('products-grid').style.display = 'grid';"
new_show_function = "function showAllProducts() { window.location.href = '/winkel/';"

old_hide_function = "function hideAllProducts() { document.getElementById('products-grid').style.display = 'none';"
new_hide_function = "function hideAllProducts() { window.location.href = '/winkel/';"

content = content.replace(old_show_function, new_show_function)
content = content.replace(old_hide_function, new_hide_function)
print("✅ Fonctions showAllProducts/hideAllProducts redirigent vers /winkel/")

# 3. Modifier toggleAllProducts pour rediriger aussi
old_toggle = "function toggleAllProducts() { const grid = document.getElementById('products-grid');"
new_toggle = "function toggleAllProducts() { window.location.href = '/winkel/'; return; const grid = document.getElementById('products-grid');"

content = content.replace(old_toggle, new_toggle)
print("✅ Fonction toggleAllProducts redirige vers /winkel/")

# 4. Supprimer un des boutons "Bekijk alle 67" en double
# Chercher et supprimer le deuxième bouton
pattern = r'(<button[^>]*onclick="toggleAllProducts\(\)"[^>]*>.*?Bekijk alle 67.*?</button>)'
matches = list(re.finditer(pattern, content, re.DOTALL | re.I))

if len(matches) > 1:
    # Supprimer le dernier
    last_match = matches[-1]
    content = content[:last_match.start()] + content[last_match.end():]
    print(f"✅ Bouton en double supprimé (il restait {len(matches)} boutons)")

# 5. Corriger les titres des produits qui ont été mal capitalisés
# Par exemple "Natuurlijke zalm Bites" → "Natuurlijke Zalm Bites"
product_names = [
    ('Natuurlijke zalm Bites', 'Natuurlijke Zalm Bites'),
    ('Biologische hertenvlees Strips', 'Biologische Hertenvlees Strips'),
    ('Natuurlijke kauwsticks', 'Natuurlijke Kauwsticks'),
    ('Gedroogde eend Bites', 'Gedroogde Eend Bites'),
    ('Mini training treats', 'Mini Training Treats'),
]

for old_name, new_name in product_names:
    content = content.replace(old_name, new_name)

print("✅ Noms de produits corrigés")

# Sauvegarder
with open(input_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("=" * 60)
print("🎉 CORRECTIONS FINALES APPLIQUÉES!")
print("=" * 60)
