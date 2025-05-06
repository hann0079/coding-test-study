def solution(n):
    answer = 0 # 더한 결과
    if n % 2 != 0:
        n -= 1
    while n > 0:
        answer += n
        n -= 2
    return answer