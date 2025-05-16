e, w = map(int,(input().split()))
adj = []

for i in range(e):
    row = []
    for j in range(e):
        row.append(0)
    adj.append(row)

for k in range(w):
    u,v,w = map(int,(input().split()))
    adj[u-1][v-1] = w

for i in adj:
    for j in i:
        print(j,end=" ")
    print()