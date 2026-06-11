import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Style professionnel
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# ============================================
# 1. CHARGEMENT ET NETTOYAGE DES DONNÉES
# ============================================

df = pd.read_csv('100 Sales Records.csv')

# Conversion des dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extraction du mois et de l'année pour l'analyse temporelle
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['YearMonth'] = df['Order Date'].dt.to_period('M')

print("Aperçu des données :")
print(df.head(3))
print(f"\nNombre total de transactions : {len(df)}")
print(f"Période : {df['Order Date'].min().date()} à {df['Order Date'].max().date()}")
print(f"Profit total : {df['Total Profit'].sum():,.2f}")

# ============================================
# 2. GRAPHIQUE 1 : PROFIT PAR RÉGION (Bar chart horizontal)
# ============================================

profit_region = df.groupby('Region')['Total Profit'].sum().sort_values()
print(profit_region.sort_values())

fig1, ax1 = plt.subplots(figsize=(12, 6))
bars = ax1.barh(profit_region.index, profit_region.values, color='yellow', edgecolor='blue')

# Ajout des valeurs sur les barres
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 50000, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}', ha='left', va='center', fontsize=10)

ax1.set_xlabel('Total Profit (€)', fontsize=12)
ax1.set_title('Profit total par région', fontsize=14, fontweight='bold')
ax1.tick_params(axis='x', labelsize=10)
plt.tight_layout()
plt.savefig('profit_par_region.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n✅ Graphique 1 sauvegardé : profit_par_region.png")

# ============================================
# 3. GRAPHIQUE 2 : ÉVOLUTION MENSUELLE DU PROFIT (Line plot)
# ============================================

# Agrégation par mois
monthly_profit = df.groupby('YearMonth')['Total Profit'].sum()
monthly_revenue = df.groupby('YearMonth')['Total Revenue'].sum()

# Conversion pour l'affichage
months = monthly_profit.index.astype(str)

fig2, ax2 = plt.subplots(figsize=(14, 6))

# Tracé des deux courbes
ax2.plot(months, monthly_profit.values, marker='o', linewidth=2,
         markersize=6, color='green', label='Total Profit')
ax2.plot(months, monthly_revenue.values, marker='s', linewidth=2,
         markersize=6, color='orange', alpha=0.7, label='Total Revenue')

# Mise en forme
ax2.set_xlabel('Mois', fontsize=12)
ax2.set_ylabel('Montant (€)', fontsize=12)
ax2.set_title('Évolution mensuelle du chiffre d\'affaires et du profit', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left')
ax2.tick_params(axis='x', rotation=45, labelsize=9)
ax2.grid(True, alpha=0.3)

# Ajout d'une ligne de tendance pour le profit
z = np.polyfit(range(len(monthly_profit)), monthly_profit.values, 1)
p = np.poly1d(z)
ax2.plot(months, p(range(len(monthly_profit))), '--', color='darkgreen',
         alpha=0.5, label='Tendance profit')

ax2.legend(loc='upper left')
plt.tight_layout()
plt.savefig('evolution_mensuelle.png', dpi=150, bbox_inches='tight')
plt.show()

print("✅ Graphique 2 sauvegardé : evolution_mensuelle.png")

# ============================================
# 4. GRAPHIQUE 3 : TOP 10 PRODUITS PAR PROFIT (Bar chart)
# ============================================

top_products = df.groupby('Item Type')['Total Profit'].sum().sort_values(ascending=False).head(10)

# Palette de couleurs
colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(top_products)))[::-1]

fig3, ax3 = plt.subplots(figsize=(12, 7))
bars = ax3.bar(top_products.index, top_products.values, color=colors, edgecolor='black')

# Ajout des valeurs sur les barres
for bar, value in zip(bars, top_products.values):
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 50000,
             f'{value:,.0f}', ha='center', va='bottom', fontsize=10, rotation=0)

ax3.set_xlabel('Type de produit', fontsize=12)
ax3.set_ylabel('Total Profit (€)', fontsize=12)
ax3.set_title('Top 10 des produits les plus rentables', fontsize=14, fontweight='bold')
ax3.tick_params(axis='x', rotation=45, labelsize=10)

plt.tight_layout()
plt.savefig('top10_produits_profit.png', dpi=150, bbox_inches='tight')
plt.show()

print("✅ Graphique 3 sauvegardé : top10_produits_profit.png")

# ============================================
# 5. ANALYSE SUPPLÉMENTAIRE (affichage dans la console)
# ============================================

print("\n" + "=" * 60)
print("📊 ANALYSE STATISTIQUE RAPIDE")
print("=" * 60)

# Meilleure région
best_region = profit_region.idxmax()
best_region_profit = profit_region.max()
print(f"\n🏆 Meilleure région : {best_region} ({best_region_profit:,.2f} € de profit)")

# Meilleur produit
best_product = top_products.index[0]
best_product_profit = top_products.iloc[0]
print(f"🏆 Produit le plus rentable : {best_product} ({best_product_profit:,.2f} €)")

# Canal le plus performant
channel_profit = df.groupby('Sales Channel')['Total Profit'].sum()
best_channel = channel_profit.idxmax()
print(f"🏆 Canal le plus rentable : {best_channel}")

# Marge moyenne par produit
df['Margin_%'] = (df['Total Profit'] / df['Total Revenue']) * 100
avg_margin = df.groupby('Item Type')['Margin_%'].mean().sort_values(ascending=False).head(5)
print("\n📈 Top 5 produits par marge moyenne (%):")
for product, margin in avg_margin.items():
    print(f"   - {product}: {margin:.1f}%")
