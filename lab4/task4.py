n, m = map(int,input().split())

u = list(map(int,input().split()))
v = list(map(int,input().split()))

adj_lst = []

for i in range(n):
    row = []
    adj_lst.append(row)

for i in range(m):
    adj_lst[u[i]-1].append(v[i])
    adj_lst[v[i]-1].append(u[i]-1)

odd = 0
for i in adj_lst:
    if len(i)%2 !=0:
        odd+= 1

if odd==0 or odd==2:
    print("YES")
else:
    print("NO")