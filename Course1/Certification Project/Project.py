import pandas as pd
import numpy as np
import datetime
import calendar

def convert(date):
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return (calendar.day_name[born])

df = pd.read_csv('DataSet.csv')
df.head()
df2 = pd.DataFrame()

df2 = df[['title','timeStamp']]
'''
dic2 = {}

daylist = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

for i in daylist:
    dic1 = {}
    for j,k in df2.iterrows():
        day = convert(k['timeStamp'].split()[0])
        if i == day:
            title = k['title'].split(':')[0]
            if title in dic1.keys():
                dic1[title] += 1
            else:
                dic1[title] = 1
    dic2[i] = dic1
print(dic2)
'''
newdataf = pd.DataFrame(columns=['title','Day'])

df3=pd.DataFrame()

df3 = df[['title','timeStamp']]

i=0
daylist = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


for j,k in df3.iterrows():
    day = convert(k['timeStamp'].split()[0])
    title = k['title'].split(':')[0]
    newdataf.loc[j] = [title,day]

print (newdataf.head())