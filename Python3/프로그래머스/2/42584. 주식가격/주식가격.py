def solution(prices):
    n = len(prices)
    stack = []
    answer = [0] * n
    
    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            v = stack.pop()
            answer[v] = i - v
        stack.append(i)
        
    while stack:
        v = stack.pop()
        answer[v] = n - 1 - v
        
    return answer