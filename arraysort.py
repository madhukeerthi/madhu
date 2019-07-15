n=int(input())
array=[]
for i in range(n):
    num=int(input())
    array.append(num)
for i in range(n):
    for j in range(i+1,n):
        if array[i]>array[j]:
            t=array[i]
            array[i]=array[j]
            array[j]=t
print(array)
