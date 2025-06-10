def solution(n):
    # answer = n // 7
    # return answer + 1 if n % 7 else answer

    p = 1
    while n // (p * 7) >= 1 and n % (p * 7):
        p += 1
    return p