from collections import deque

def find_furthest(start, adj_list, size):
    distance = [-1] * (size + 1)
    distance[start] = 0
    queue = deque([start])
    furthest_node = start

    while queue:
        current = queue.popleft()
        for neighbor in adj_list[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
                if distance[neighbor] > distance[furthest_node]:
                    furthest_node = neighbor
    return furthest_node, distance[furthest_node]

num_nodes = int(input())
edges = [[] for _ in range(num_nodes + 1)]

for _ in range(num_nodes - 1):
    a, b = map(int, input().split())
    if 1 <= a <= num_nodes and 1 <= b <= num_nodes:
            edges[a].append(b)
            edges[b].append(a)

first_node, _ = find_furthest(1, edges, num_nodes)
second_node, max_distance = find_furthest(first_node, edges, num_nodes)

print(max_distance)
print(first_node, second_node)