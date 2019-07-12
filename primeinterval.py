n1=int(input())
n2=int(input())
for n in range(n1,n2+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
