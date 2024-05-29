import pandas as pd
 
# Load the provided Excel file
file_path = '../data/_cluster_data_.xlsx'
df_clusters = pd.read_excel(file_path)
 
# Display the first few rows to understand the structure
df_clusters.head()

# Compute the correlation matrix
correlation_matrix_clusters = df_clusters.corr()
 
# Plot the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix_clusters, annot=False, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix for Clusters and Features')
plt.show()