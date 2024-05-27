from collections import deque

def solution(board):
    
    dr = [0, 1,  0, -1]
    dc = [1, 0, -1,  0]
    n = len(board)
    
    def in_range(r1, c1, r2, c2):
        return 0 <= r1 < n and 0 <= c1 < n and 0 <= r2 < n and 0 <= c2 < n
            
    q = deque()
    visited = set()
    q.append((0, 0, 0, 1, 0))
    visited.add((0, 0, 0, 1))
    
    while q:
        cur_one_r, cur_one_c, cur_two_r, cur_two_c, cur_sec = q.popleft()
        
        if cur_one_r == n-1 and cur_one_c == n-1 or cur_two_r == n-1 and cur_two_c == n-1:
            return cur_sec
        
        for i in range(4):
            nor, noc, ntr, ntc = cur_one_r + dr[i], cur_one_c + dc[i], cur_two_r + dr[i], cur_two_c + dc[i]
            if in_range(nor, noc, ntr, ntc) and (nor, noc, ntr, ntc) not in visited \
            and board[nor][noc] == 0 and board[ntr][ntc] == 0:
                q.append((nor, noc, ntr, ntc, cur_sec + 1))
                visited.add((nor, noc, ntr, ntc))
    
        if cur_one_r == cur_two_r : # 가로일 때
            for j in (-1, 1):
                nor, ntr = cur_one_r + j, cur_two_r + j
                if in_range(nor, cur_one_c, ntr, cur_two_c) and board[nor][cur_one_c] == 0 and board[ntr][cur_two_c] == 0:
                    if (cur_one_r, cur_one_c, nor, cur_one_c) not in visited:
                        q.append((cur_one_r, cur_one_c, nor, cur_one_c, cur_sec + 1)) 
                        visited.add((cur_one_r, cur_one_c, nor, cur_one_c))
                    if (ntr, cur_two_c, cur_two_r, cur_two_c) not in visited:
                        q.append((ntr, cur_two_c, cur_two_r, cur_two_c, cur_sec + 1)) 
                        visited.add((ntr, cur_two_c, cur_two_r, cur_two_c))
                        
        elif cur_one_c == cur_two_c: # 세로일 때
            for j in (-1, 1):
                noc, ntc = cur_one_c + j, cur_two_c + j
                if in_range(cur_one_r, noc, cur_two_r, ntc) and board[cur_one_r][noc] == 0 and board[cur_two_r][ntc] == 0:
                    if (cur_one_r, cur_one_c, cur_one_r, noc) not in visited:
                        q.append((cur_one_r, cur_one_c, cur_one_r, noc, cur_sec + 1))
                        visited.add((cur_one_r, cur_one_c, cur_one_r, noc))
                    if (cur_two_r, ntc, cur_two_r, cur_two_c) not in visited:    
                        q.append((cur_two_r, ntc, cur_two_r, cur_two_c, cur_sec + 1)) 
                        visited.add((cur_two_r, ntc, cur_two_r, cur_two_c))

    return -1

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))