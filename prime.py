c=int(input())
x=0
if c>1:
    for i in range(2,c+1):
        if c%i==0:
            x+=1
    if x==1:
        print("prime")
    else:
        print("not prime")
else:
    print("not prime")
 
