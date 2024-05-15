a=int(input("Enter a no.:"))
def fn(x):
    flag=0
    if(x>1):
        for i in range(2,x):
            if(x%i==0):
                flag=1
    else:
        flag=2
    if flag==0:
        print(x," is a prime no.")
    elif(flag==2):
        print("1 is neither prime nor composite")
    else:
        print(x," is not a prime no.")
   
fn(a)
