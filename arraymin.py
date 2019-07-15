n=int(input())
array=[]
for i in range(n):
    num=int(input())
    array.append(num)
min=array[0]
for i in range(n):
    if array[i]<min:
        min=array[i]
print(min)
