def solution(sizes):
    big = [max(s) for s in sizes]
    small = [min(s) for s in sizes]
    return max(big) * max(small)