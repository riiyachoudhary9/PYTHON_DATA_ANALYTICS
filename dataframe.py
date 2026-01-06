import pandas as pd
data={['a','b','c','d'],[80,90,85,94]}
df=pd.DataFrame(data)
data.columns=['name','scores']
print(df)

