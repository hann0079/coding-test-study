from itertools import combinations
from collections import deque
import sys

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

virus = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
answer = sys.maxsize

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(com):
    q = deque()
    for r, c in com:
        q.append((r, c, 0))
    tmp = [grid[i][:] for i in range(n)]
    max_sec = 0

    while q:
        cur_r, cur_c, cur_sec = q.popleft()
        for k in range(4):
            next_r, next_c, next_sec = cur_r + dr[k], cur_c + dc[k], cur_sec + 1
            if in_range(next_r, next_c):
                if tmp[next_r][next_c] == ' ':
                    tmp[next_r][next_c] = next_sec
                    max_sec = max(max_sec, next_sec)
                    q.append((next_r, next_c, next_sec))
                elif tmp[next_r][next_c] == '*':
                    tmp[next_r][next_c] = next_sec
                    q.append((next_r, next_c, next_sec))

    after = 0
    for idx in range(n):
        after += tmp[idx].count(' ')

    return max_sec if after == 0 else -1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            grid[i][j] = ' '
        elif grid[i][j] == 1:
            grid[i][j] = '-'
        else:
            grid[i][j] = '*'
            virus.append((i, j))

for com in combinations(virus, m):
    for row, col in com:
        grid[row][col] = 0
    result = bfs(com)
    answer = min(answer, result) if result != -1 else answer
    for row, col in com:
        grid[row][col] = '*'

answer = -1 if answer == sys.maxsize else answer
print(answer)