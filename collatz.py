
b=int(input("enter a number"))
i=0
while True:
    
    if(b%2==0):
        b=(b/2)
        i+=1
        print(b)
        if(b==1):
            break
        
    
    else:
        b=b*3+1
        i+=1
        print(b)
        if(b==1):
            break
        
        
print("number of steps    ",i)    