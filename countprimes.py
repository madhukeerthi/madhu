l,u=int(input()),int(input())
count=0
for n in range(l,u + 1):
   if  n> 1:
       for j in range(2,n):
           if (n%j) == 0:
               break
       else:
           count+=1
print(count)
