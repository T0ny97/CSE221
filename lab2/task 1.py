len,target = map(int,input().split())
arr = list(map(int,input().split()))

l = 0
r = len - 1
flag = False
while l<r:
    sum = arr[l] + arr[r]
    if sum==target:
        l, r  = l+1, r+ 1
        print(l," ",r)
        flag= True
        break
    elif sum<target:
        l += 1
    else:
        r -= 1

if not flag:
    print(-1)
