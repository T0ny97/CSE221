def minsort(arr):
    cnt = 0
    temp = 0

    for i in range(len(arr)):
        temp = i
        for j in range(i+1, len(arr)):
            if arr[j][1] > arr[temp][1]:
                temp = j
            elif arr[j][1] == arr[temp][1] and arr[j][0] < arr[temp][0]:
                temp = j

        if temp != i:
            arr[i],arr[temp] = arr[temp],arr[i]
            cnt = cnt + 1
    return cnt

N = int(input())
id = input().split()

for i in range(N):
    id[i] = int(id[i])

marks = input().split()
for i in range(N):
    marks[i] = int(marks[i])

output = []
for i in range(N):
    output.append((id[i], marks[i]))


counter = minsort(output)
print(f'Minimum swaps: {counter}')

for i in range(N):
    print(f'ID: {output[i][0]} Mark: {output[i][1]}' )