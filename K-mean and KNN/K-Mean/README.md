# K-Means Clustering Algorithm

## Overview

**K-Means** is an **unsupervised machine learning algorithm** used to partition a dataset into **K distinct clusters**. Each data point is assigned to the cluster whose **centroid** is closest, based on a chosen distance metric. The algorithm aims to group similar data points together while maximizing the separation between different clusters.

K-Means is widely used due to its simplicity, efficiency, and scalability.

---

## Distance Measure

The most commonly used distance metric in K-Means is the **Euclidean distance**.

**Given:**

- A data point:
$$\mathbf{x} = (x_1, x_2, \dots, x_d)$$

- A cluster centroid:
$$\mathbf{c} = (c_1, c_2, \dots, c_d)$$

The Euclidean distance is defined as:

$$
d(\mathbf{x}, \mathbf{c}) = \sqrt{\sum_{i=1}^{d} (x_i - c_i)^2}
$$

This distance is used to determine which centroid is closest to each data point during the assignment step.

---

## Objective Function

K-Means minimizes the **Within-Cluster Sum of Squared Distances (WCSS)**:

$$
J = \sum_{k=1}^{K} \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \boldsymbol{\mu}_k\|^2
$$

Where:
- $K$ is the number of clusters  
- $C_k$ is the set of points assigned to cluster $k$ 
-  $\boldsymbol{\mu}_k$ is the centroid of cluster $k$
---

## Algorithm Steps

### 1. Initialization
Randomly select $K$ data points as the initial centroids.

### 2. Assignment Step
For each data point:
- Compute the distance to all centroids
- Assign the point to the cluster with the nearest centroid

### 3. Update Step
Recalculate each centroid as the mean of the data points assigned to that cluster:

$$
\boldsymbol{\mu}_k = \frac{1}{|C_k|} \sum_{\mathbf{x} \in C_k} \mathbf{x}
$$

### 4. Convergence
Repeat the assignment and update steps until:
- Centroids no longer change significantly
- Cluster assignments remain stable
- A predefined maximum number of iterations is reached

---

## Advantages

- Simple and intuitive
- Fast and computationally efficient
- Scales well to large datasets
- Easy to implement

---

## Limitations

- The number of clusters $K$ must be specified in advance
- Sensitive to the initial placement of centroids
- Performs poorly with non-spherical or overlapping clusters
- Sensitive to noise and outliers

---

## Applications

K-Means is commonly used in:
- Customer segmentation
- Image segmentation
- Data compression
- Pattern recognition
- Exploratory data analysis

---

## Conclusion

> K-Means is useful algorithm for gathering groups when you know the number of cluster AND IT IS NOT THE SAME AS KNN
---
--- 


# KMeans Clustering – Step-by-step Visualization

## 1. Data Initialization

At the beginning, **500 data points** are generated randomly in a 2D space.  
These points are distributed following predefined Gaussian distributions to simulate naturally clustered data.

At this stage:
- All data points are unlabeled.
- No clustering structure is imposed yet.
- The visualization only reflects the raw spatial distribution of the dataset.

This step serves as the input for the KMeans clustering algorithm.

📌 **Figure 1 – Initial random data distribution**  
<img width="642" height="478" alt="image" src="https://github.com/user-attachments/assets/fbc7affe-9a59-4625-a0f3-88855966ecd0" />

---

## 2. Attempt to Label for Data – Iteration 0

In the first attempt (Iteration 0):
- Initial cluster centers are randomly selected from the dataset.
- All data points are assigned to the nearest center based on Euclidean distance.

Because the centers are initialized randomly:
- Cluster assignments are still rough.
- Some clusters may overlap.
- The boundaries between clusters are not well defined.

This step represents the **initial assignment phase** of KMeans.

📌 **Figure 2 – Initial labeling (Iteration 0)**  
<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/f8e866f9-93a2-47d4-bddd-42b9cc8cbdd0" />

---

## 3. Attempt to Label for Data – Iteration 1

After the first reassignment:
- Cluster centers are updated by computing the mean of all points assigned to each cluster.
- Data points are reassigned based on the updated centers.

Compared to Iteration 0:
- Cluster shapes become more coherent.
- Points start to gather around more reasonable centroids.
- Misclassified points begin to move toward the correct clusters.

This iteration shows the **early refinement stage** of the algorithm.

📌 **Figure 3 – Iteration 1: Label assignment**  
<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/3f7827c8-dbc7-4244-ac7c-8bea3a06d199" />

📌 **Figure 4 – Iteration 1: Updated cluster centers**  
<img width="638" height="552" alt="image" src="https://github.com/user-attachments/assets/df81f12f-fbb4-481b-ab39-afb1e259596e" />

---

## 4. Attempt to Label for Data – Iteration 2

In Iteration 2:
- The updated centers better represent the true structure of the data.
- Reassignments are fewer compared to earlier iterations.

Observations:
- Clusters are more compact.
- Separation between clusters becomes clearer.
- The movement of centers is smaller than in previous iterations.

This indicates that the algorithm is approaching convergence.

📌 **Figure 5 – Iteration 2: Label assignment**  
<img width="634" height="483" alt="image" src="https://github.com/user-attachments/assets/5b4923e6-51b6-453b-ac13-6cf7108b88e4" />

📌 **Figure 6 – Iteration 2: Updated cluster centers**  
<img width="635" height="481" alt="image" src="https://github.com/user-attachments/assets/17167fb1-213e-415b-83b2-ce82bad4d0c7" />

---

## 5. Attempt to Label for Data – Iteration 3

At this stage:
- Only a small number of points change their cluster assignment.
- Centers shift slightly as they fine-tune their positions.

The clustering structure is now:
- Stable
- Visually well-separated
- Close to the optimal solution

This iteration demonstrates the **late optimization phase** of KMeans.

📌 **Figure 7 – Iteration 3: Label assignment**  
<img width="635" height="479" alt="image" src="https://github.com/user-attachments/assets/78ec28ef-e50e-40d7-8c8a-aa921b7df2e2" />

📌 **Figure 8 – Iteration 3: Updated cluster centers**  
<img width="636" height="481" alt="image" src="https://github.com/user-attachments/assets/7616ef99-14b8-4315-ab69-7a642afb1566" />

---

## 6. Attempt to Label for Data – Iteration 4

Iteration 4 shows minimal visual change compared to Iteration 3:
- Most points remain in the same clusters.
- Center movement is very small.

This suggests that:
- The algorithm is nearly converged.
- Further iterations will not significantly improve the result.

📌 **Figure 9 – Iteration 4: Label assignment**  
<img width="641" height="482" alt="image" src="https://github.com/user-attachments/assets/f8fcf231-b73d-43df-965b-dfb7ea726ad4" />

📌 **Figure 10 – Iteration 4: Updated cluster centers**  
<img width="638" height="477" alt="image" src="https://github.com/user-attachments/assets/fc6ca0ff-8794-4e2c-93ff-79571115d514" />

---

## 7. Attempt to Label for Data – Iteration 5

At this point:
- Cluster assignments remain almost identical to the previous iteration.
- Centers have effectively stabilized.

The clustering result is now:
- Consistent
- Reproducible
- Suitable to be considered converged

📌 **Figure 11 – Iteration 5: Label assignment**  
<img width="631" height="475" alt="image" src="https://github.com/user-attachments/assets/ce5ffddb-7d31-43bb-986b-7800bb43100f" />

📌 **Figure 12 – Iteration 5: Updated cluster centers**  
<img width="631" height="474" alt="image" src="https://github.com/user-attachments/assets/e32c0507-075e-4192-9ef0-fc49d167c2a1" />

---

## 8. Attempt to Label for Data – Iteration 6 (Convergence)

In Iteration 6:
- No significant changes in cluster assignments occur.
- The centers no longer move beyond a small tolerance threshold.

This indicates that the **KMeans algorithm has converged**.

Final result:
- Each data point belongs to one of the clusters.
- Cluster centers represent the mean position of their assigned points.
- The algorithm terminates successfully.

📌 **Figure 13 – Final clustering result**  
<img width="643" height="482" alt="image" src="https://github.com/user-attachments/assets/0f60c58a-f604-4d22-bdf8-4aaefa0f8083" />

---

## 9. Summary

Through multiple iterations, KMeans:
1. Initializes cluster centers randomly
2. Assigns data points to the nearest center
3. Updates centers based on current assignments
4. Repeats until convergence

The visualizations clearly demonstrate how cluster structure evolves from random initialization to a stable and well-separated configuration.
