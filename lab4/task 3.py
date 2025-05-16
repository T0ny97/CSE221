e = int(input())
adj = []

for i in range(e):
    row = []
    for j in range(e):
        row.append(0)
    adj.append(row)

for vert in range(e):
    st = list(map(int,input().split()))
    if st[0]==0:
        continue
    for con in st[1:]:
        adj[vert][con] = 1

for i in adj:
    for j in i:
        print(j,end=" ")
    print()