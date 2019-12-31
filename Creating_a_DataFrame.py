#Creating a Pandas DataFrame
import pandas as pd
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df=pd.DataFrame(lst)
# print(df)


#Creating DataFrame from dict of ndarray/lists

data = {'Name':['Tom', 'nick', 'krish', 'jack'],'Age':[20, 21, 19, 18]}
df=pd.DataFrame(data)
# print(df)


#Dealing with Rows and Columns
#Selecting Colum to be displayed

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],'Age':[27, 24, 22, 32],'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
# print(df)


dic={
    "engagedly-services": "staging_july_2109",
    "enquete": "engagedly_UI_revised_staging__config_as_env_var",
    "audit-subscriber": "staging_july_2109",
    "augadh": "qa_dec_2019",
    "bharga": "events_common_branch",
    "durjaya": "engagedly_UI_revised_staging_config_as_env_var",
    "eauth-services": "staging_july_2109_config_as_env_var",
    "ekaksha": "engagedly_UI_revised_staging_config_as_env_var",
    "elastic-interface": "engagedly_UI_revised_staging_ebm_nov_config_as_env_var",
    "engagedly": "engagedly_UI_revised_ebm_dec_config_as_env_var",
    "faye-server": "staging_july_2109",
    "advaya": "engagedly_UI_revised_staging_config_as_env_var",
    "aja": "es6_data_push","ananta": "develop",
    "anmolhrm": "engagedly_UI_revised_abhinev_staging_ebm_dec_config_as_env_var",
    "api-gateway": "staging_july_2109_config_as_env_var",



}
key_list=list(dic.keys())
value_list=list(dic.values())
# print(key_list)
# print(value_list)
dic={}
dic["application"]=key_list
dic["branch"]=value_list
# print(dic)
df=pd.DataFrame(dic)
df.sort_values(by=['application'], ascending=True,)
df.reset_index(drop=True,inplace=True)
# print(df)
rows,column=df.shape
# print(" number os rows is "+ str(rows)+" \n"+ "number of column is "+ str(column))

# print(df.head(2))
# print(df[4:7])
# print(df.columns)
# print(df["application"])
# print(type(df["branch"]))
print(df["application"])