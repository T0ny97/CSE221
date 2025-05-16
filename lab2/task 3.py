len,target = map(int,input().split())
arr = list(map(int,input().split()))

len1 = 0  # 
sum = 0 
l = 0 

for i in range(len):

    sum += arr[i]
        

    while sum > target and l <= i:
        sum -= arr[l]
        l += 1
        

    if sum <= target:
        len1 = max(len1, i - l + 1)

print(len1)