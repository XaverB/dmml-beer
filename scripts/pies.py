import matplotlib.pyplot as plt
import pandas as pd
 
# Data
clusters = {
    'Cluster 1': {'Brut': 1},
    'Cluster 2': {'Kriek': 7, 'Lambic': 4, 'West Flanders ale': 4, 'Flanders old brown': 3, 'Faro': 2, 'Fruitbeer': 1},
    'Cluster 3': {'Hoppy': 4, 'Saison': 1, 'Blond': 1, 'Strong ale': 1},
    'Cluster 4': {'Fruitbeer': 6, 'Kriek': 4, 'Lambic': 3, 'Christmas': 2, 'West Flanders ale': 2, 'Scotch': 2, 'Low/No alcohol': 1, 'Wheat': 1, 'Saison': 1, 'Faro': 1, 'Stout/Porter': 1, 'Brown': 1, 'Strong ale': 1, 'Brut': 1, 'Blond': 1, 'Tripel': 1},
    'Cluster 5': {'Blond': 13, 'Tripel': 10, 'Hoppy': 8, 'Strong ale': 6, 'Saison': 5, 'Stout/Porter': 5, 'Brown': 4, 'Brett/cofermented': 3, 'Amber': 3, 'Wheat': 2, 'Flanders old brown': 1, 'Brut': 1, 'Pils/Lager': 1, 'Christmas': 1},
    'Cluster 6': {'Strong ale': 10, 'Stout/Porter': 4, 'Christmas': 3, 'Hoppy': 2, 'Scotch': 2, 'Brown': 2, 'Tripel': 2, 'Dubbel': 1, 'Amber': 1, 'Brut': 1},
    'Cluster 7': {'Blond': 19, 'Tripel': 15, 'Amber': 8, 'Wheat': 8, 'Pils/Lager': 6, 'Low/No alcohol': 6, 'Dubbel': 6, 'Brown': 4, 'Stout/Porter': 2, 'Christmas': 2, 'West Flanders ale': 1, 'Saison': 1}
}

# Plotting pie charts for each cluster
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
axes = axes.flatten()
 
for i, (cluster, beers) in enumerate(clusters.items()):
    ax = axes[i]
    labels = beers.keys()
    sizes = beers.values()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(cluster)
 
# Hide any unused subplots
for j in range(i + 1, len(axes)):
    axes[j].axis('off')
 
plt.tight_layout()
plt.show()