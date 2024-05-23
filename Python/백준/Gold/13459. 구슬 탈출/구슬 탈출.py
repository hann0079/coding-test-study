from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
answer = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j, 0)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            goal = (i, j)

visited = set()
q = deque()
visited.add((red[0], red[1], blue[0], blue[1]))
q.append((red[0], red[1], blue[0], blue[1], 1))

while q:
    cur_r, cur_c, cur_br, cur_bc, cur_count = q.popleft()
    if cur_count > 10:
        break
    for i in range(4):
        next_r, next_c, cnt_r = cur_r, cur_c, 0
        next_br, next_bc, cnt_b = cur_br, cur_bc, 0
        while board[next_r + dr[i]][next_c + dc[i]] not in ('#', 'O'):
            next_r += dr[i]
            next_c += dc[i]
            cnt_r += 1
        while board[next_br + dr[i]][next_bc + dc[i]] not in ('#', 'O'):
            next_br += dr[i]
            next_bc += dc[i]
            cnt_b += 1

        if (next_br + dr[i], next_bc + dc[i]) == goal:
            continue
        if (next_r + dr[i], next_c + dc[i]) == goal:
            answer = 1
            break

        if next_r == next_br and next_c == next_bc:
            if cnt_r > cnt_b:
                next_r -= dr[i]
                next_c -= dc[i]
            else:
                next_br -= dr[i]
                next_bc -= dc[i]

        if (next_r, next_c, next_br, next_bc) not in visited:
            q.append((next_r, next_c, next_br, next_bc, cur_count+1))
            visited.add((next_r, next_c, next_br, next_bc))
    else:
        continue
    break
print(answer)