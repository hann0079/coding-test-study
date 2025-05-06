def solution(n):
    answer = 2
    result = n**(1/2) 
    if result == int(result):
        answer = 1
    return answer