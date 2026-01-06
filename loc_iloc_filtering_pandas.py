import pandas as pd
import matplotlib.pyplot as plt
stud_list=[['saksham',36,75,5420000],['vansh',38,74,3420000],['payal',31,70,8428000],
           ['sharad',34,80,4428000],['chitra',40,100,4528000],['john',33,72,7028000],['kunal',42,85,2528000]]
df=pd.DataFrame(stud_list,columns=['name','age','weight','salary'])
print(df)
df1=df.iloc[0:4]
print(df1)
df1=df.iloc[:0:3]
print(df1)
data=df[df['age']>35].iloc[:,:]
print(data)


scores={'name':['a','b','c','d'],'score':[90,80,95,20]}
df=pd.DataFrame(scores)
print(df)
plt.bar(df['name'],df['score'])
plt.show()





