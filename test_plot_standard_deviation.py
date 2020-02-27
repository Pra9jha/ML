import pandas as pd, seaborn as sns,matplotlib.pyplot as plt ,math
data={"data":[2,3,5,6,8,9,12,34,56],"stdev":[]}
sum=0
for element in data["data"]:
    sum=sum+element
mean=sum/len(data["data"])
length=len(data["data"])

# for i in data["data"]:
#     data["stdev"].append(abs(i-mean))
# print(data["data"])
# print(data["stdev"])
# sns.lineplot(data["data"],data["stdev"])
# plt.show()

#
# for i in data["data"]:
#     data["stdev"].append(math.sqrt(pow(i-mean,2)))
# print(data["data"])
# print(data["stdev"])
# sns.lineplot(data["data"],data["stdev"])
# plt.show()

dev=0
for data in data["data"]:
    dev=dev+pow(data-mean,2)
std_dev=math.sqrt(dev/length)

for i in [2,3,5,6,8,9,12,34,56]:
    data["stdev"].append(math.sqrt(pow(i-std_dev,2)))
print(data["data"])
print(data["stdev"])
sns.lineplot(data["data"],data["stdev"])
plt.show()