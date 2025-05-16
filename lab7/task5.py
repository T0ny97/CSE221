import heapq
n,m = map(int,input().split())

adj = [[] for _ in range(n+1)]
st = list(map(int,input().split()))
end = list(map(int,input().split()))
w = list(map(int,input().split()))

for i in range(len(st)):
    adj[st[i]].append((end[i],w[i]))

def shortest_distance_with_parity(adj, s, n):
    
    dist = [[float('inf')] * 2 for _ in range(len(adj))]
    dist[s][0] = 0
    dist[s][1] = 0

    q = [(0, s, -1)] 

    while q:
        current_dist, u, last_parity = heapq.heappop(q)

        for v, weight in adj[u]:
            curr_parity = weight % 2

            if curr_parity == last_parity:
                continue  
            if current_dist + weight < dist[v][curr_parity]:
                dist[v][curr_parity] = current_dist + weight
                heapq.heappush(q, (dist[v][curr_parity], v, curr_parity))

    ans = min(dist[n][0], dist[n][1])
    return ans if ans != float('inf') else -1

result = shortest_distance_with_parity(adj, 1, n)
print(result)