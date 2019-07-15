n=int(input())
array=[]
for i in range(n):
    num=int(input())
    array.append(num)
max=array[0]
for i in range(n):
    if array[i]>max:
        max=array[i]
print(max)
