import pandas as pd

#Read Salary.csv as a dataframe called sal
print("********************** Printing dataframe **********************")
sal=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Salaries.csv")

print(sal)

#Check the head of the dataframe
print("**********************Printing Head***************************")
print(sal.head(2))

#Use info method to find out number of entries
print("*************************** To use info method to find number of entries ***************************")
print(sal.info())

#Average Base Salary
print("*************************** Average base salary ***************************")
print(sal["BasePay"].mean())

#Highest amount of overtime pay
print("********************** Highest amount of overtime pay **********************")
print(sal["OvertimePay"].max())

#Job title of Joseph Driscoll
print("*****************Job title of Joseph Driscoll ***************************************")
print(sal[sal["EmployeeName"]=="Joseph Driscoll"]["JobTitle"])

#How much does Joseph Driscoll make (including benifits)
print("***************** How much does Joseph Driscoll make (including benifits) *****************")
salary_data=(sal[["EmployeeName","BasePay","OvertimePay","OtherPay","Benefits","TotalPay","TotalPayBenefits"]])
print(salary_data[salary_data["EmployeeName"]=="Joseph Driscoll"].sum(axis=1))



#Name of Highest paid person (including benifits)
print("***************Name of Highest paid person (including benifits) *******************")
print(sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].max()][["EmployeeName","TotalPayBenefits"]])


#Name of Least paid person (including benifits)
print("***************Name of Least paid person (including benifits) *******************")
print(sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].min()][["EmployeeName","TotalPayBenefits"]])


#what was BasePay of all the employee per year ? (2011-2014)
print("what was BasePay of all the employee per year ? (2011-2014)")
sal_groupby=sal.groupby("Year").mean()["BasePay"]
print(sal_groupby)


#How many unique job title are there
print("* **************************How many unique job title are there****************************")
print(sal["JobTitle"].unique())
print(sal["JobTitle"].nunique()) # or
print(len(sal["JobTitle"].unique()))


#Top 5 most common job
print("* ************************** Top 5 most common job ****************************")
print(sal["JobTitle"].value_counts().head())




# dic=[{"name":"Prashant","skill":["python","devops"],"city":"Bangalore",},{"name":"Prabhat","skill":["Python","ML","Great in Mathematics"],"city":"Delhi"}]
# data_frame=pd.DataFrame(dic)
# print(data_frame)