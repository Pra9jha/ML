'''K mean cluster for two mean '''

import random

def mean(cluster_list):
    length=len(cluster_list)
    sum=0
    for element in cluster_list:
        sum=sum+element
    return round(sum/length,0)


def k_mean_clustering(list,random_mean):
    cluter1=[]
    cluster2=[]
    # print(list)
    # print(random_mean)
    for element in list:
        if abs(random_mean[0]-element)>abs(random_mean[1]-element):
            cluster2.append(element)
        else:
            cluter1.append(element)
    # print(cluter1)
    # print(cluster2)
    # print("********************************************")
    mean_value=[mean(cluter1),mean(cluster2)]
    # print(mean_value)
    if mean_value==random_mean:
        print("Cluster value is ")
        print(cluter1)
        print(cluster2)
        return 0
    k_mean_clustering(list,mean_value)


list=[2,3,4,10,11,12,20,25,30]

random_mean=[]
while True:
    M=random.randrange(len(list))
    if list[M] not in random_mean:
        random_mean.append(list[M])
    if len(random_mean)==2:
        break
k_mean_clustering(list,random_mean)
