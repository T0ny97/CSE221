
def min_height_bst(arr, l, r, result):
    if l > r:
        return
    mid = (l + r) // 2 
    result.append(arr[mid])   
    min_height_bst(arr, l, mid - 1, result)  
    min_height_bst(arr, mid + 1, r, result)


N = int(input())
arr = list(map(int, input().split()))
l = 0
r = N-1
result = []
min_height_bst(arr, l, r, result)

print(*result)