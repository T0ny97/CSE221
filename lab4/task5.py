n,m = map(int,input().split())

u = list(map(int,input().split()))
v = list(map(int,input().split()))

lst = []
for i in range(n):
    lst.append([0,0])


for j in range(m):
    inn = u[j] - 1
    out = v[j] - 1
    lst[inn][0] = lst[inn][0] + 1
    lst[out][1] = lst[out][1]+ 1

for k in lst:
    diff = k[1] - k[0]
    print(diff,end=" ")