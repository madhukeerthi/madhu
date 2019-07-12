n=int(input())
n1=n
sum=0
while n>0:
    r=n%10
    sum+=r**3
    n=n//10
if(n1==sum):
    print("Yes")
else:
    print("No")
