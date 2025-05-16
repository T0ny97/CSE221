def find_root(parent, x):
    root = x
    while parent[root] != root:

        root = parent[root]

    while x != root:
        next = parent[x]
        parent[x] = root
        x = next

    return root

def merge(parent, size, x, y):
    tx = find_root(parent, x)
    ty = find_root(parent, y )
    if tx != ty:
        if size[tx]< size[ty]:
            tx, rty = ty, tx

        parent[ty] = tx

        size[tx] += size[ty]

    return size[tx]


n, k = map(int, input().split())
parent = [i for i in range(n +1)]

size = [1]* (n +1)

for i in range(k):
    a, b = map(int, input().split())
    print(merge(parent, size, a, b))