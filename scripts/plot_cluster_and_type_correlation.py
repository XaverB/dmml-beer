import matplotlib.pyplot as plt

# Define the data for each cluster
clusters = {
    'Cluster 1': {'Brut': 1},
    'Cluster 2': {'Kriek': 7, 'Lambic': 4, 'West Flanders ale': 4, 'Flanders old brown': 3, 'Faro': 2, 'Fruitbeer': 1},
    'Cluster 3': {'Hoppy': 4, 'Saison': 1, 'Blond': 1, 'Strong ale': 1},
    'Cluster 4': {'Fruitbeer': 6, 'Kriek': 4, 'Lambic': 3, 'Christmas': 2, 'West Flanders ale': 2, 'Scotch': 2,
                  'Low/No alcohol': 1, 'Wheat': 1, 'Saison': 1, 'Faro': 1, 'Stout/Porter': 1, 'Brown': 1,
                  'Strong ale': 1, 'Brut': 1, 'Blond': 1, 'Tripel': 1},
    'Cluster 5': {'Blond': 13, 'Tripel': 10, 'Hoppy': 8, 'Strong ale': 6, 'Saison': 5, 'Stout/Porter': 5, 'Brown': 4,
                  'Brett/cofermented': 3, 'Amber': 3, 'Wheat': 2, 'Flanders old brown': 1, 'Brut': 1, 'Pils/Lager': 1,
                  'Christmas': 1},
    'Cluster 6': {'Strong ale': 10, 'Stout/Porter': 4, 'Christmas': 3, 'Hoppy': 2, 'Scotch': 2, 'Brown': 2,
                  'Tripel': 2, 'Dubbel': 1, 'Amber': 1, 'Brut': 1},
    'Cluster 7': {'Blond': 19, 'Tripel': 15, 'Amber': 8, 'Wheat': 8, 'Pils/Lager': 6, 'Low/No alcohol': 6,
                  'Dubbel': 6, 'Brown': 4, 'Stout/Porter': 2, 'Christmas': 2, 'West Flanders ale': 1, 'Saison': 1}
}

# Create subplots for each cluster
num_clusters = len(clusters)
num_cols = 2
num_rows = (num_clusters + num_cols - 1) // num_cols

fig, axs = plt.subplots(num_rows, num_cols, figsize=(16, 8 * num_rows))
fig.suptitle('Beer Type Distribution by Cluster', fontsize=10, y=0.95)

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.9, wspace=0.6)

# Iterate over each cluster and create a bar plot
for i, (cluster, data) in enumerate(clusters.items()):
    row = i // num_cols
    col = i % num_cols
    
    beer_types = list(data.keys())
    counts = list(data.values())

    axs[row, col].bar(beer_types, counts)
    axs[row, col].set_title(cluster, fontsize=9)
    axs[row, col].set_ylabel('Count', fontsize=8)
    axs[row, col].tick_params(axis='x', rotation=45, labelsize=4)

# Remove empty subplots
for i in range(num_clusters, num_rows * num_cols):
    row = i // num_cols
    col = i % num_cols
    fig.delaxes(axs[row, col])

# Display the plot
plt.show()