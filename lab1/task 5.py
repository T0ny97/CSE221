def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag==False:
            break

N = int(input())
inp = input().split()
for i in range(N):
    inp[i] = int(inp[i])

bubbleSort(inp) 
for i in inp:
    print(i,end = " ")