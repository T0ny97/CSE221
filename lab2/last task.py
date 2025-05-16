

def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left  

def upper_bound(arr, y):
   
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= y:
            left = mid + 1
        else:
            right = mid
    return left - 1 


n, q = map(int, input().split())
arr = list(map(int, input().split()))


for _ in range(q):
    x, y = map(int, input().split())

    l = lower_bound(arr, x)  
    r = upper_bound(arr, y)
    
    print(max(0, r - l + 1))
