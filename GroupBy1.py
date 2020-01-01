import pandas as pd
company_product={}
company_product["Company"]=["GooG","GooG","MSFT","MSFT","FB","FB"]
company_product["person"]=["Sam","Charline","Amy","Vanessa","Carl","Sarah"]
company_product["stales"]=[200,120,340,124,243,350]
df=pd.DataFrame(company_product)
# df.columns=list(company_product.keys())

# print(df)


g=df.groupby("Company")
print(g)

for i,j in g:
    print(i)
    print(j)
    print("*******************")


#
# #shows sum of sale by all company
# print(g.sum())
# #Only sum of sale by FB
# print(g.sum().loc["FB"])









# print(g.mean())
# print(g.max())
# print(g.std())
# print(g.describe())