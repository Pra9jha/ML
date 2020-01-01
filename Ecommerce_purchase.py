import pandas as pd
df=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Ecommerce_Purchases.csv")
print(df.head())
print(df.info())

#How many rows and columns are there
print("***************************** How many rows and columns are there *****************************")
r,c=df.shape
print("Number of rows is "+ str(r))
print("Number of columns is "+str(c))

#Average purchase price ?
print("***************************** Average purchase price ? *****************************")
print(df["Purchase Price"].mean())

#Highest and Lowest purchase price ?
print("***************************** Highest and Lowest purchase price ? *****************************")
print(df["Purchase Price"].max())
print(df["Purchase Price"].min())

#How many people have english en as as their Language of choice on the website  ?
print("***************************** How many people have english en as as their Language of choice on the website ***************************** ")
print(df[df["Language"]=="en"]["Language"].count())

#How many people have job title as "Lawyer"
print("****************************  How many people have job title as Lawyer ****************************")
print(df[df["Job"]=="Lawyer"]["Job"].count())

#How many people made purchase during AM and how many people made the purcahase during PM
print("How many people made purchase during AM and how many people made the purcahase during PM")
print(df["AM or PM"].value_counts())
# print(df[df["AM or PM"]=="PM"]["AM or PM"].count())

#What is the email of persion with credit card number  4926535242672853
print("************************  hat is the email of persion with credit card number  4926535242672853 ************************")
print(df[df["Credit Card"]==4926535242672853]["Email"])

#How many people have American Express as their Credit card provider and make a purchase above $95 ?
print("************************How many people have American Express as their Credit card provider and make a purchase above $95 ?************************")

#How many people have credit card that expires on 2025
print("How many people have credit card that expires on 2025")
lst=[i[3:] for i in df["CC Exp Date"]]

print(lst.count("25"))