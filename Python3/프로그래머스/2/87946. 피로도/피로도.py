def solution(k, dungeons):
    
    def backtrack(k, cnt):
        nonlocal answer 
        if cnt > answer:
            answer = cnt
            
        for i in range(n):
            if k >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                backtrack(k - dungeons[i][1], cnt + 1)
                visited[i] = False
    
    answer = 0
    n = len(dungeons)
    visited = [False] * n
    backtrack(k, 0)
    
    return answer