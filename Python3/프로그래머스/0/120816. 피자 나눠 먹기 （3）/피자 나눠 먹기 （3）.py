def solution(slice, n):
    r = n % slice
    d = n // slice
    if r:
        d += 1
    return d