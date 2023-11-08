l1=[2,4,6,8,2,6]
l2=[1,1,3,5,7]
l1.extend(l2)
l3=[]
for i in range(len(l1)):
    x=l1[i]
    y=l1.count(x)
    l3.append(y)
i=0
j=0
length=len(l1)
while length<0:
    print(f"i={i}")
    while length<0:
        print(f"j={j}")
        if l1[i]==l1[j]:
            if i!=j:
                l1.pop(j)
                l3.pop(j)
                length=length-1
        j=j+1
    i=i+1
    
dict={}
for i in range(len(l1)):   
    dict[l1[i]]=l3[i]      
print(dict)
            
