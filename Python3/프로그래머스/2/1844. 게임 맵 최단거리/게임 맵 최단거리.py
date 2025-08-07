from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, start_v):
    n = len(graph)
    m = len(graph[0])
    
    q = deque()
    q.append(start_v)
    
    visited = [[False]*m for _ in range(n)]
    visited[start_v[0]][start_v[1]] = True

    while q:
        x, y = q.popleft()
        
        if x == n-1 and y == m-1:
            return graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return -1

def solution(maps):
    return bfs(maps, (0, 0))
