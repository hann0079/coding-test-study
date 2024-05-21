from itertools import combinations
from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
virus, empty = [], []
answer = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == 0:
            empty.append((r,c))
        elif grid[r][c] == 2:
            virus.append((r,c))


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs():
    global answer
    tmp = [grid[i][:] for i in range(n)]
    q = deque(virus)
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if in_range(next_r, next_c):
                if tmp[next_r][next_c] == 0:
                    tmp[next_r][next_c] = 2
                    q.append((next_r, next_c))
    cnt = 0
    for i in tmp:
        cnt += i.count(0)
    answer = max(answer, cnt)


for wall in combinations(empty, 3):
    for r, c in wall:
        grid[r][c] = 1
    bfs()
    for r, c in wall:
        grid[r][c] = 0

print(answer)