len1 = int(input())
arr1 = list(map(int,input().split()))

len2 = int(input())
arr2 = list(map(int,input().split()))

# len1,len2 = 3,6
# arr1 = [2,10,12]
# arr2 = [3 ,4, 6, 7, 8, 9]


output = []
m,n = 0,0

for i in range(len1+len2):
    if arr1[m]<arr2[n]:
        output.append(arr1[m])
        m+= 1
        if m == len1:
            arr1.append(arr2[len2-1]+1)
    else:
        output.append(arr2[n])
        n+= 1
        if n==len2:
            arr2.append(arr1[len1-1]+1)

for j in output:
    print(j,end=" ")