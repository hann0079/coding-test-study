from collections import deque

def solution(places):
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    n = 5
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n

    def bfs(idx, r, c):
        q = deque()
        q.append((r, c, 0))
        while q:
            cur_r, cur_c, cur_dis = q.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if in_range(next_r, next_c):
                    if next_r == r and next_c == c:
                        continue
                    next_dis = cur_dis + abs(cur_r - next_r) + abs(cur_c - next_c)
                    if next_dis > 2:
                        return
                    if places[idx][next_r][next_c] == 'P':
                        return 0
                    elif places[idx][next_r][next_c] == 'X':
                        continue
                    q.append((next_r, next_c, next_dis))
    
    answer = [1] * 5
    for idx in range(5): # 대기실 개수 
        for i in range(5): # 대기실 내부
            for j in range(5):
                if places[idx][i][j] == 'P':
                    if bfs(idx, i, j) == 0:
                        answer[idx] = 0
                        
    return answer
