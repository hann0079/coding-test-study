from collections import deque

def solution(board):
    n = len(board)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n

    def is_empty(r, c):
        return in_range(r, c) and board[r][c] == 0

    def can_move(r1, c1, r2, c2):
        return is_empty(r1, c1) and is_empty(r2, c2)

    def add(q, visited, r1, c1, r2, c2, sec):
        state = (r1, c1, r2, c2)
        if state not in visited:
            visited.add(state)
            q.append((r1, c1, r2, c2, sec))

    q = deque([(0, 0, 0, 1, 0)])
    visited = set([(0, 0, 0, 1)])

    while q:
        r1, c1, r2, c2, sec = q.popleft()

        if (r1, c1) == (n-1, n-1) or (r2, c2) == (n-1, n-1):
            return sec

        # 직선 이동
        for dr, dc in directions:
            nr1, nc1, nr2, nc2 = r1 + dr, c1 + dc, r2 + dr, c2 + dc
            if can_move(nr1, nc1, nr2, nc2):
                add(q, visited, nr1, nc1, nr2, nc2, sec + 1)

        # 회전
        if r1 == r2:  # 가로 상태
            for d in (-1, 1):
                if is_empty(r1 + d, c1) and is_empty(r2 + d, c2):
                    add(q, visited, r1, c1, r1 + d, c1, sec + 1)
                    add(q, visited, r2, c2, r2 + d, c2, sec + 1)
        elif c1 == c2:  # 세로 상태
            for d in (-1, 1):
                if is_empty(r1, c1 + d) and is_empty(r2, c2 + d):
                    add(q, visited, r1, c1, r1, c1 + d, sec + 1)
                    add(q, visited, r2, c2, r2, c2 + d, sec + 1)

    return -1
