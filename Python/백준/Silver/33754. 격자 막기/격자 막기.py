import sys
from collections import deque

N = int(sys.stdin.readline())
grid_row1 = list(map(int, sys.stdin.readline().split()))
grid_row2 = list(map(int, sys.stdin.readline().split()))

grid = [grid_row1, grid_row2]

ones = []
for i in range(2):
    for j in range(N):
        if grid[i][j] == 1:
            ones.append((abs(i - 0) + abs(j - 0), (i, j)))

ones.sort()

def check(k):
    current_grid = [[grid[i][j] for j in range(N)] for i in range(2)]

    for i in range(1, len(ones)):
        if i > k:
            break
        r, c = ones[i][1]
        if (r, c) == (0, 0) or (r, c) == (1, N - 1):
            continue
        current_grid[r][c] = 0

    q = deque([(0, 0)])
    visited = [[False] * N for _ in range(2)]
    visited[0][0] = True

    while q:
        r, c = q.popleft()

        if (r, c) == (1, N - 1):
            return False

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < 2 and 0 <= nc < N and current_grid[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

    return True

low = 0
high = len(ones) - 2
ans = high

while low <= high:
    mid = (low + high) // 2
    if check(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)