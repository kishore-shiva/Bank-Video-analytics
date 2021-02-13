import pandas as pd
import numpy as np
import datetime

df = pd.read_excel('data.xlsx')
now = datetime.datetime.now()
hour=now.hour

hour_list=list(df['Name'])
name_list=list(df['Hour'])
df.loc[len(df)+1]=["kishore",10]

df.to_excel('data.xlsx',index = False)

print(df)
print('len is : ',df['Name'])