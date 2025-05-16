n, m = map(int,(input().split()))

u = list(map(int,input().split()))
v=  list(map(int,input().split()))
w =  list(map(int,input().split()))

adj_lst = []
for i in range(n):
    adj_lst.append([])

for i in range(m):
    adj_lst[u[i]-1].append((v[i],w[i]))

for k in range(len(adj_lst)):
    j = k+1
    sr = ""
    for l in adj_lst[k]:
        sr += str(l) + " "
    print(f"{j}: {sr}")