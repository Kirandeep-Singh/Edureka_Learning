li = [12,24,35,70,88,120,155]

A=[x for i,x in enumerate(li) if i not in (0,4,5)]

B=[li[i] for i in range(0,len(li)) if i not in (0,4,5)]

print (A == B)
