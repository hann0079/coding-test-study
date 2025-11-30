def solution(park, routes):
    answer = []
    Up=len(park)
    Side=len(park[0])
    for i in range(len(park)):
        if 'S' in park[i]:
            y=park[i].index('S')
            x=i

    for j in range(len(routes)):
        direction,distance=routes[j][0],int(routes[j][2])
        if direction=='S':
            if x+distance<Up:
                for i in range(1, distance+1):
                    if park[x+i][y]=='X':
                        break
                else:
                    x+=distance
        elif direction=='W':
            if y-distance>=0:
                for i in range(1, distance+1):
                    if park[x][y-i]=='X':
                        break
                else:
                    y-=distance
        elif direction=='E':
            if y+distance<Side:
                for i in range(1, distance+1):
                    if park[x][y+i]=='X':
                        break
                else:
                    y+=distance
        elif direction=='N':
            if x-distance>=0:
                for i in range(1, distance+1):
                    if park[x-i][y]=='X':
                        break 
                else: # 반복 정상 종료 시 실행 (break로 강제 종료 X)
                    x -= distance
    answer=[x,y]
    return answer