import pandas as pd,seaborn as sns,numpy as np,matplotlib.pyplot as plt
#
#
x=np.array([[5,3,1],[10,15,2],[15,12,3],[24,10,4],[30,45,5],[85,70,6],[71,80,7],[60,78,18],[55,52,9],[80,91,0]])

# print(x[:,0])
# print("****************")
# print(x[:,1])
# print("****************")
# print(x[:,2])
# sns.scatterplot(x[:,0],x[:,1],x[:,2])
# plt.show()

from sklearn.cluster import KMeans


elbow_finding=[]
for k in range(1,6):
    km = KMeans(n_clusters=k)
    km.fit(x)
    elbow_finding.append(km.inertia_)
print(elbow_finding)

# sns.lineplot(range(1,6),elbow_finding)
# plt.show()
#here for this dataset k=2 is the elbow point

kmeans = KMeans(n_clusters=2)
kmeans.fit(x)
print(kmeans.cluster_centers_)
print(kmeans.labels_)

