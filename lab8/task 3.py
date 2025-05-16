class UnionFind:
    def __init__(self, size):
        self.leader = list(range(size))
        self.depth = [1] * size

    def trace(self, x):
        if self.leader[x] != x:
            self.leader[x] = self.trace(self.leader[x])
        return self.leader[x]

    def connect(self, a, b):
        rootA = self.trace(a)
        rootB = self.trace(b)
        if rootA == rootB:
            return False
        if self.depth[rootA] < self.depth[rootB]:
            self.leader[rootA] = rootB
        elif self.depth[rootA] > self.depth[rootB]:
            self.leader[rootB] = rootA
        else:
            self.leader[rootB] = rootA
            self.depth[rootA] += 1
        return True

def find_largest_below(u, target, bound, graph, visited, marker):
    stack = [(u, -1)]
    while stack:
        current, heaviest = stack.pop()
        if current == target:
            return heaviest
        if visited[current] == marker:
            continue
        visited[current] = marker
        for neighbor, weight in graph[current]:
            if visited[neighbor] != marker:
                highest = heaviest
                if weight < bound and weight > heaviest:
                    highest = weight
                stack.append((neighbor, highest))
    return -1

def second_best_tree(n_nodes, edge_list):
    edge_list.sort()
    uf = UnionFind(n_nodes)
    mst_total = 0
    tree = [[] for _ in range(n_nodes)]
    taken = [False] * len(edge_list)

    for idx, (cost, a, b) in enumerate(edge_list):
        if uf.connect(a, b):
            taken[idx] = True
            mst_total += cost
            tree[a].append((b, cost))
            tree[b].append((a, cost))

    if sum(taken) != n_nodes - 1:
        return -1

    seen = [0] * n_nodes
    counter = 1
    alt_total = float('inf')

    for idx, (cost, a, b) in enumerate(edge_list):
        if taken[idx]:
            continue
        counter += 1
        max_in_path = find_largest_below(a, b, cost, tree, seen, counter)
        if max_in_path != -1:
            candidate_cost = mst_total - max_in_path + cost
            if candidate_cost > mst_total:
                alt_total = min(alt_total, candidate_cost)

    return -1 if alt_total == float('inf') else alt_total

# Input parser
nodes, connections = map(int, input().split())
all_edges = []
for _ in range(connections):
    x, y, z = map(int, input().split())
    all_edges.append((z, x - 1, y - 1))

print(second_best_tree(nodes, all_edges))