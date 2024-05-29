# dmml-beer

## General

We analyze the beer data set to apply things we learned during data mining and machine learning.

Our starting task is to build a beer recommendation engine. We want to cluster the beers by their aroma attributes and join the overall score of the beer to the results. So, if someone likes beer `X`, we are able to recommend similar tasting beers to him.

## Aroma attributes

After analyzing the data set 7 and reading the paper, we will use following attributes to categorize beers by their taste. We removed all cumulated attributes.

- A_malt_grain
- A_malt_bread
- A_malt_cara
- A_malt_burn
- A_hops_citrus
- A_hops_tropical
- A_hops_noble
- A_hops_woody
- A_esters_ethac
- A_esters_isoaa
- A_esters_flower
- A_esters_fruity
- F_malt_grain
- F_malt_bread
- F_malt_cara
- F_malt_burn
- F_hops_citrus
- F_hops_tropical
- F_hops_noble
- F_hops_woody
- F_esters_ethac
- F_esters_isoaa
- F_esters_flower
- F_esters_fruity
- acidity
- bitternes
- sweetness
- X4vg
- diacetyl
- dms
- metallic
- stale_hops
- t2n
- orange
- coriander
- clove
- lactic
- acetic
- barnyard
- aftertaste
- co2

## Clustering

At first we experiment with heuristic lab and k mean. Then we were able to create our first clusters with the desired target variables.

Now we want to find the right cluster size. For this we are using the elbow method.

Elbow Method:

- Run k-means clustering on the data for a range of k values (e.g., 1 to 10).
- For each k, calculate the sum of squared distances between data points and their cluster centroid (inertia or within-cluster sum of squares).
- Plot the inertia against the number of clusters k.
- Look for the "elbow point" in the plot where the rate of decrease in inertia slows down significantly.
- Choose the k value at the elbow point as the optimal number of clusters.

The results are plotted with heuristic lab:

![elbow_cluster](./assets/elbow_cluster.png)

We choose a cluster size of 8.



## Creating our result

The we preceded by creating a data set of the clustering result + beer_id + beer_type.

Now we can take a look if the clusters are similar to the beer types.



## Questions

Interesting questions which arose during the study:

- Does clustering by aroma correlate to the type of beer (like pale ale etc.?