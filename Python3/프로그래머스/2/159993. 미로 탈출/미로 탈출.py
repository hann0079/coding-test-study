from collections import deque

def is_valid_move(nr, nc, n, m, maps):
    return 0 <= nr < n and 0 <= nc < m and maps[nr][nc] != 'X'

def append_to_queue(nr, nc, k, time, visited, q):
    if not visited[nr][nc][k]:
        visited[nr][nc][k] = True
        q.append((nr, nc, k, time + 1))

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q = deque()
    end_r, end_c = -1, -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                q.append((i, j, 0, 0))
                visited[i][j][0] = True
            if maps[i][j] == 'E':
                end_r, end_c = i, j
    
    while q:
        r, c, k, time = q.popleft()
        
        # 출구 도달, 레버 당겼으면 탈출
        if r == end_r and c == end_c and k == 1:
            return time 
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not is_valid_move(nr, nc, n, m, maps):
                continue
            if maps[nr][nc] == 'L':
                append_to_queue(nr, nc, 1, time, visited, q)
            else:
                append_to_queue(nr, nc, k, time, visited, q)
                
    return -1