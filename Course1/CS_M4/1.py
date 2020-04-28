def prob(*args):
    lt=[]
    for i in args:
        i=round((2*50*i/30)**0.5)
        lt.append(str(i))
    print (','.join(lt))

prob(100,150,180)
