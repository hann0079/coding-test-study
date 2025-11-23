def solution(s):
    count_p = 0
    count_y = 0
    for c in s:
        if c == 'P' or c == 'p':
            count_p += 1
        elif c == 'Y' or c == 'y':
            count_y += 1
    return True if count_p == count_y else False