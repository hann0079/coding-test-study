from collections import deque

def solution(board):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    n = len(board)
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    def can_move(r1, c1, r2, c2):
        return in_range(r1, c1) and in_range(r2, c2) and board[r1][c1] == 0 and board[r2][c2] == 0
    
    def add_state(q, visited, r1, c1, r2, c2, sec):
        if ((r1, c1, r2, c2) not in visited):
            q.append((r1, c1, r2, c2, sec))
            visited.add((r1, c1, r2, c2))

    q = deque([(0, 0, 0, 1, 0)])
    visited = set([(0, 0, 0, 1)])
    
    while q:
        r1, c1, r2, c2, sec = q.popleft()
        
        if (r1 == n-1 and c1 == n-1) or (r2 == n-1 and c2 == n-1):
            return sec
        
        for i in range(4):
            nr1, nc1, nr2, nc2 = r1 + dr[i], c1 + dc[i], r2 + dr[i], c2 + dc[i]
            if can_move(nr1, nc1, nr2, nc2):
                add_state(q, visited, nr1, nc1, nr2, nc2, sec + 1)
        
        if r1 == r2:
            for d in (-1, 1):
                if in_range(r1 + d, c1) and in_range(r2 + d, c2) and board[r1 + d][c1] == 0 and board[r2 + d][c2] == 0:
                    add_state(q, visited, r1, c1, r1 + d, c1, sec + 1)
                    add_state(q, visited, r2, c2, r2 + d, c2, sec + 1)
        elif c1 == c2:
            for d in (-1, 1):
                if in_range(r1, c1 + d) and in_range(r2, c2 + d) and board[r1][c1 + d] == 0 and board[r2][c2 + d] == 0:
                    add_state(q, visited, r1, c1, r1, c1 + d, sec + 1)
                    add_state(q, visited, r2, c2, r2, c2 + d, sec + 1)

    return -1
