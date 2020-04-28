import pandas as pd
import numpy as np

''' Problems wiht File SalaryGender.csv 
df = pd.read_csv('SalaryGender.csv')
arr_sal = np.asarray(df['Salary'], float)
arr_gender = np.asarray(df['Gender'])
arr_age = np.asarray(df['Age'])
arr_phd = np.asarray(df['PhD'])
#print (df)

### Prob 1 All Columns to NP Array ###
arr_sal = np.asarray(df['Salary'], float)
arr_gender = np.asarray(df['Gender'])
arr_age = np.asarray(df['Age'])
arr_phd = np.asarray(df['PhD'])

### Prob 2 No. of men with PhD and Women with PhD ###
men=1
women=0
menc=0
womenc=0
for i in range(0,100):
    if arr_gender[i] == 1 and arr_phd[i] == 1:
        menc+=1
    elif arr_gender[i] == 0 and arr_phd[i] == 1:
        womenc+=1

print ('Count of Men with PhD is {}'.format(menc))
print ('Count of WoMen with PhD is {}'.format(womenc))

### Prob 3 ###
frame = pd.DataFrame()
frame['Age'] = arr_age
frame['PhD'] = arr_phd

for i in range(0,100):
    if frame.loc[i]['PhD'] == 0:
        frame = frame.drop(i)

print (frame)

### Prob 4 ###
countphd=0
for i in range(0,100):
    if arr_phd[i] == 1:
        countphd += 1

print ('Count of People with PHD is {}'.format(countphd))
'''
'''
### Prob 5 ###
arr = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
lt = []

for i in set(arr):
    cnt = 0
    for j in arr:
        if i == j:
            cnt+=1
    lt.append(cnt)

out = np.asarray(lt)

a = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
print (np.bincount(a))
'''

'''
### Prob 6 ###

a = np.array([[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]])
print (a[a>5])
### Prob 7 ###
a = np.array([ np.nan, 1., 2., np.nan, 3., 4., 5.])
lt = []
for i in range(0,len(a)):
    if not np.isnan(a[i]):
        lt.append(a[i])
print(np.asarray(lt))
or in one go
print (a[~np.isnan(a)]
### Prob 8 ###
a = np.random.random((10,10))
print (a.max())
print (a.min())
'''




























