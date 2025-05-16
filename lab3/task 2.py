N = int(input())
arr = list(map(int,input().split()))

def pair_max(arr):
    n = len(arr)
    max_value = float('-inf')
    i = 0  
    
    for j in range(1, n):
        max_value = max(max_value, arr[i] + arr[j]**2)
        val = max(arr[i], arr[j])
        i = arr.index(val)
    
    return max_value

output = pair_max(arr)
print(output)