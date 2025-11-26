def solution(park, routes):
    nav = {
        'S': (1,0),
        'N': (-1, 0),
        'W': (0, -1),
        'E': (0,1)        
    }
    h, w = len(park), len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j
    
    for route in routes:
        direction, distance = route[0], int(route[2])
        next_x, next_y = x, y
        dx, dy = nav[direction][0], nav[direction][1]
        for i in range(distance):
            next_x += dx
            next_y += dy
            if not (0 <= next_x < h) or not (0 <= next_y < w) or park[next_x][next_y] == 'X':
                break
        else:
            x, y = next_x, next_y
        
    return [x, y]