def solution(dirs):
    answer = 0
    grid = [[0] * 11 for _ in range(11)]
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    dict_s = {'U': 0, 'D': 1, 'L': 2 , 'R': 3}
    
    x, y = 5, 5
    grid[x][y] = 1
    path = set()
    
    for s in dirs:
        
        next_x = x + dxs[dict_s[s]]
        next_y = y + dys[dict_s[s]]
        
        if (0 <= next_x <= 10 and 0 <= next_y <= 10):
            if (x, y, next_x, next_y) not in path:
                path.add((x, y, next_x, next_y))
                path.add((next_x, next_y, x, y))
                answer += 1
            x, y = next_x, next_y

    return answer