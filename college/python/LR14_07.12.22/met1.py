import itertools
sl1=input ('Введіть слово 1 =')
sl2=input ('Введіть слово 2 =')
m=len(sl1); n=len(sl2); i=0; L=[]

while m!=i:
    fl=0
    for j in itertools. count (start=0, step=1) :
        if j>=n: 
            break
        if j<n:
            if sl1[i]==sl2[j]: 
                fl=1
        if fl==1:
            L.append ( 'так')
        else:
            L.append ("ні")
    i+=1
a=list(L)
pp= ' '.join (a) ; print (pp)