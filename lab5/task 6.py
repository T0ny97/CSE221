from collections import deque
r,c = map(int,input().split())

rows = []
for i in range(r):
    o = input()
    b = []
    for i in o:
        b.append(i)
    rows.append(b)

visited = [[0]*c for _ in range(r)]

def Dchecker(grid, visited, i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    res = 0

    while q:
        x, y = q.popleft()

        if grid[x][y] == 'D':
            res += 1

        for x1, y1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x2, y2 = x + x1, y + y1
            if 0 <= x2 < r and 0 <= y2 < c and grid[x2][y2] != '#' and visited[x2][y2] == 0:
                visited[x2][y2] = 1
                q.append((x2, y2))
    
    return res


output = []
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] != '#' and visited[i][j] == 0:
            output.append(Dchecker(rows, visited, i, j))
        

print(max(output))