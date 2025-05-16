import sys
sys.setrecursionlimit(2 * 10**5 + 10)
read = sys.stdin.readline

n_nodes, root = map(int, read().split())
adj = [[] for _ in range(n_nodes + 1)]


for _ in range(n_nodes - 1):
    a, b = map(int, read().split())
    adj[a].append(b)
    adj[b].append(a)

subtree = [0] * (n_nodes + 1)

def compute(curr, parent):
    subtree[curr] = 1
    for neighbor in adj[curr]:
        if neighbor != parent:
            compute(neighbor, curr)
            subtree[curr] += subtree[neighbor]

compute(root, -1)

num_queries = int(read())
for _ in range(num_queries):
    node = int(read())
    print(subtree[node])