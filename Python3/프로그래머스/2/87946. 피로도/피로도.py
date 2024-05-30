def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [0] * n
    
    def backtrack(k, cnt):
        nonlocal answer
        
        if cnt > answer:
            answer = cnt
        
        for i in range(n):
            if k >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                backtrack(k - dungeons[i][1], cnt + 1)
                visited[i] = False
                
    backtrack(k, 0)
    return answer