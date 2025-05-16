def find_root(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]

        x = parent[x]


    return x


def merge( parent, rank, x, y):
    rtx = find_root(parent, x)
    rty = find_root(parent, y )
    if rtx == rty:
        return False
    
    if rank[rtx]< rank[rty]:
        parent[rtx] = rty

    elif rank[rtx]> rank[rty]:
        parent[rty] = rtx

    else:
        parent[rty] = rtx
        rank[rtx] +=1

    return True



def kruskal(n, edge, ex = None):

    parent = [ i for i in range(n+1 )]

    rank = [0]*(n+1)
    total = 0
    visited = 0
    var = []

    for idx, (w,x,y ) in enumerate(edge):
        if ex != None and idx == ex:
            continue

        if merge(parent, rank, x,y):
            total += w
            visited += 1
            var.append(idx)


            if visited == n-1:
                break

    if visited != n-1:
        return None

    return total, var


def second(n, edge):
    edge.sort()
    ran = kruskal(n, edge)
    if not ran:
        return -1
    
    total, edge2 = ran
    best2 = float('inf')

    for idx in edge2:
        x = kruskal(n, edge, idx)

        if x:
            p, q = x

            if p > total and  p< best2:

                best2 = p
    
    return best2 if best2 != float('inf') else -1



n,m = map(int, input().split())

edge = []

for i in range(m):
     x, y, w = map(int, input().split())
     edge.append((w, x, y))


print((second(n, edge)))