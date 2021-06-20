
import pandas as pd
data = pd.read_csv("happyscore_income.csv")
happy = data["happyScore"]
income = data["GDP"]
import matplotlib.pyplot as plt

plt.xlabel("GDP")
plt.ylabel ("Happiness")
plt.scatter(income, happy)

from sklearn.cluster import KMeans
import numpy as np
income_happy = np.column_stack((income,happy))
km_res = KMeans(n_clusters=3).fit(income_happy)
clusters= km_res.cluster_centers_
plt.scatter(clusters[:,0],clusters[:,1], s=1250, alpha=0.5)
plt.text(clusters[0,0],clusters[0,1],"Medium GDP/High Happiness Cluster")
plt.text(clusters[1,0],clusters[1,1],"Low GDP/Low Happiness Cluster")
plt.text(clusters[2,0],clusters[2,1],"High GDP/High Happiness Cluster")