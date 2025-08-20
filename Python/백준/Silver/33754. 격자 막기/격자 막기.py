from collections import deque

N = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
grid = [row1, row2]

def bfs(g):
    if g[0][0] == 0 or g[1][N-1] == 0:
        return False
    q = deque([(0,0)])
    visited = [[False]*N for _ in range(2)]
    visited[0][0] = True
    while q:
        x,y = q.popleft()
        if (x,y) == (1,N-1):
            return True
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<2 and 0<=ny<N and not visited[nx][ny] and g[nx][ny]==1:
                visited[nx][ny] = True
                q.append((nx,ny))
    return False

if not bfs(grid):
    print(0)
    exit()

for i in range(2):
    for j in range(N):
        if (i,j) in [(0,0),(1,N-1)]:
            continue
        if grid[i][j] == 1:
            grid[i][j] = 0
            if not bfs(grid):
                print(1)
                exit()
            grid[i][j] = 1

print(2)
