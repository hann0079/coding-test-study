from collections import deque
import sys

input = sys.stdin.readline
#✅ 입력 형식에 맞춰서 입력값을 받는다.
n, m = map(int,input().split())
board = [input().rstrip() for _ in range(n)]


answer = 0
queue = deque()
visited = set()
#✅ 빨간 구슬과 파란 구슬의 위치를 저장한다.
for r in range(n):
    for c in range(m):
        if board[r][c] == "R":
            rr, rc = r, c
        elif board[r][c] == "B":
            br, bc = r, c
            
queue.append([rr, rc, br, bc, 1])
visited.add((rr, rc, br, bc))

def print_init(board, rr, rc, br, bc):
    board[rr] = board[rr][:rc] + '.' + board[rr][rc+1:]
    board[br] = board[br][:bc] + '.' + board[br][bc+1:]

def move(r, c, dr, dc):
    count = 0
    while board[r+dr][c+dc] != "#" and board[r][c] != "O":
        r += dr
        c += dc
        count += 1
    return r, c, count
#✅ 두 구슬의 초기 위치를 시작으로 BFS 알고리즘을 수행한다.
while queue:
    cur_rr, cur_rc, cur_br, cur_bc, level = queue.popleft()
		#✅ 움직임 횟수가 10을 초과하면 반복문을 종료한다.
    if level > 10:
        break
    for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
				#✅ 기울이는 방향에 따른 두 구슬의 다음 위치를 구한다.
        next_rr, next_rc, r_count = move(cur_rr, cur_rc, dr, dc)
        next_br, next_bc, b_count = move(cur_br, cur_bc, dr, dc)
				#✅ 두 구슬의 다음 위치가 이미 방문했던 위치라면, 다른 방향으로 기울이기를 시도한다.
        if (next_rr, next_rc, next_br, next_bc) in visited:
            continue
				#✅ 파란 구슬의 다음 위치가 구멍이라면, 다른 방향으로 기울이기를 시도한다.
        if board[next_br][next_bc] == 'O':
            continue
				#✅ 빨간 구슬의 다음 위치가 구멍이라면, 반복문을 종료한다.
        if board[next_rr][next_rc] == 'O':
            answer = 1
            break
				#✅ 두 구슬의 다음 위치가 동일할 때, 이동 횟수가 더 많은 구슬의 위치를 한 칸 뒤로 이동한다.
        if next_rr == next_br and next_rc == next_bc:
            if r_count > b_count:
                next_rr -= dr
                next_rc -= dc
            else:
                next_br -= dr
                next_bc -= dc
        queue.append([next_rr, next_rc, next_br, next_bc, level+1])
				#✅ 두 구슬의 다음 위치를 방문했다고 표시한다.
        visited.add((next_rr, next_rc, next_br, next_bc))
    else:
        continue
    break
#✅ 성공 여부에 따라서 1 또는 0을 출력한다.
print(answer)