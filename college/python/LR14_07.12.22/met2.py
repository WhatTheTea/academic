sl1=input ('Baedith choBo 1 =')
sl2=input ('BBeniTh cnoBo 2 =')
m=len(sl1)
i=0; L= [ ]
while m!=i:
    f1=0
    if sl1[i] in sl2: 
        fl=1
    if fl==1:   
        L.append ('так')
    else:
        L.append ( 'ні')
    i+=1
a=list(L); pp="".join(a) 
print (pp)