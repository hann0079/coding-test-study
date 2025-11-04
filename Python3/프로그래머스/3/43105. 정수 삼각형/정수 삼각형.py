def solution(triangle):
    for r in range(1, len(triangle)):
        for c in range(len(triangle[r])):
            if c == 0:
                triangle[r][c] += triangle[r-1][c]
            elif c == r:
                triangle[r][c] += triangle[r-1][c-1]
            else:
                triangle[r][c] += max(triangle[r-1][c-1], triangle[r-1][c])
    return max(triangle[-1])