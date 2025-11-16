def solution(a, b):
    s, e = min(a, b), max(a, b)
    return sum(range(s,e+1))