import pandas as pd
import matplotlib.pyplot as plt

x = [a for a in range(20)]
y = [i for i in x]

'''
plt.plot(x , x)
plt.plot(x , [y**2 for y in x],)
plt.plot(x , [y**3 for y in x])
plt.plot(x , [y**4 for y in x])
plt.grid(True)
plt.xlabel('Scores')
plt.ylabel('Age')
plt.title('Graph by KD')
plt.xlim(0,20)
plt.ylim(0,1000)
#plt.show()
'''
plt.figure(figsize=(5,5))
plt.scatter(x,y)
plt.plot(x,y, 'g')
plt.hist(x,y)
plt.show()




