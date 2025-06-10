def solution(n):
    p = 1
    while n // (p * 7) > 1: 
        p += 1
    while p * 7 < n:
        p += 1
    return p