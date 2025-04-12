from collections import deque

# 입력 처리
R = int(input())
C = int(input())
grid = [list(input().strip()) for _ in range(R)]
a = int(input())
b = int(input())

# 점수 매핑
score_map = {'S': 1, 'M': 5, 'L': 10}

# 방문 체크
visited = [[False]*C for _ in range(R)]

# BFS 준비
queue = deque()
queue.append((a, b))
visited[a][b] = True
total_value = 0

# 상하좌우 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()
    
    # 점수 누적
    if grid[x][y] in score_map:
        total_value += score_map[grid[x][y]]

    # 인접 칸 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and grid[nx][ny] != '*':
                visited[nx][ny] = True
                queue.append((nx, ny))

print(total_value)
