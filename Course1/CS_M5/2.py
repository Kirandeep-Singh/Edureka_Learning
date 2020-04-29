import pandas as pd
import numpy as np
fnames = ['MathScoreTerm1.csv', 'DSScoreTerm1.csv', 'PhysicsScoreTerm1.csv']
#dfm = pd.read_csv('MathScoreTerm1.csv')
exclude = ['Name','Ethinicity']
#dfp = pd.read_csv('PhysicsScoreTerm1.csv', na_values=0)
df = pd.DataFrame()

for i in fnames:
    tmp = pd.DataFrame()
    tmpdf = pd.read_csv(i)
    for j in tmpdf.columns:
        if j not in exclude:
            tmp[j] = tmpdf[j]
    try:
        tmp['Score'] = tmp['Score'].fillna(0)
    except KeyError:
        pass
    df = df.append(tmp, ignore_index=True)

df.to_csv('Concatenated.csv', index=False)

print (df['Score'].mean())