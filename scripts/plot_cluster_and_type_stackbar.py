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
 
# Convert to dataframe
df = pd.DataFrame(clusters).fillna(0)
 
# Plot
fig, ax = plt.subplots(figsize=(10, 6))
 
df.plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Beer Types Distribution Across Clusters')
ax.set_xlabel('Beer Types')
ax.set_ylabel('Counts')
plt.legend(title='Clusters')
plt.xticks(rotation=90)
plt.tight_layout()
 
plt.show()