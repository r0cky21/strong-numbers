#strong number--

n=int(input("enter number"))
n1=n

sm=0

while(n!=0):
    rem=n%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    sm=sm+f
    n=n//10

if(n1==sm):
    print(f"{n1} is a strong number")

else:
    print(f"{n1} is not a strong number")
