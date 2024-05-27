from collections import deque

def solution(board):
    
    one_dr = [0, 1,  0, -1,  0,  0,  0,  0, 1, -1,  1, 1]
    one_dc = [1, 0, -1,  0,  0,  0,  0,  0, 1,  1, -1, 1]
    two_dr = [0, 1,  0, -1, -1,  1, -1, -1, 0,  0,  0, 0]
    two_dc = [1, 0, -1,  0, -1, -1,  1, -1, 0,  0,  0, 0 ]
    n = len(board)
    sec = 100 * 100
    
    def in_range(r1, c1, r2, c2):
        return 0 <= r1 < n and 0 <= c1 < n and 0 <= r2 < n and 0 <= c2 < n
            
    q = deque()
    visited = set()
    q.append((0, 0, 0, 1, 0))
    visited.add((0, 0, 0, 1))
    while q:
        cur_one_r, cur_one_c, cur_two_r, cur_two_c, cur_sec = q.popleft()
        for i in range(12):
            if cur_one_r != cur_two_r and i in (4, 5, 8, 9): # 가로 회전일 때 가로가 아니라면
                continue
            elif cur_one_c != cur_two_c and i in (6, 7, 10, 11): # 세로 회전일 때 세로가 아니라면 
                continue
            next_one_r = cur_one_r + one_dr[i]
            next_one_c = cur_one_c + one_dc[i]
            next_two_r = cur_two_r + two_dr[i]
            next_two_c = cur_two_c + two_dc[i]
            if i == 4 or i == 5:
                if in_range(next_one_r, next_one_c + 1, next_two_r, next_two_c + 1):
                    if board[next_one_r][next_one_c + 1] and board[next_two_r][next_two_c + 1]:
                        continue
            elif i == 6 or i == 7:
                if in_range(next_one_r - 1, next_one_c, next_two_r - 1, next_two_c):
                    if board[next_one_r - 1][next_one_c] and board[next_two_r - 1][next_two_c]:
                        continue
            elif i == 8 or i == 9:
                if in_range(next_one_r, next_one_c - 1, next_two_r, next_two_c - 1):
                    if board[next_one_r][next_one_c - 1] and board[next_two_r][next_two_c - 1]:
                        continue
            elif i == 10 or i == 11:
                if in_range(next_one_r + 1, next_one_c, next_two_r + 1, next_two_c):
                    if board[next_one_r + 1][next_one_c] and board[next_two_r + 1][next_two_c]:
                        continue

            if in_range(next_one_r, next_one_c, next_two_r, next_two_c):
                if (next_one_r, next_one_c, next_two_r, next_two_c) not in visited:
                    if board[next_one_r][next_one_c] == 0 and board[next_two_r][next_two_c] == 0:
                        q.append((next_one_r, next_one_c,   next_two_r, next_two_c, cur_sec + 1))
                        visited.add((next_one_r, next_one_c, next_two_r, next_two_c))
                        if (next_one_r == n - 1 and next_one_c == n - 1) or (next_two_r == n - 1 and next_two_c == n - 1):
                            sec = min(sec, cur_sec + 1)
                            

    return sec

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))