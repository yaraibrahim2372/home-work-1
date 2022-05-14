x=int(input("enter a decimal number"))
r=0
l=[]
while(x!=0):
    r=x%2
    x=x//2
    l=[r]+l
for i in range(0,len(l)):
    print(l[i],end='')    
