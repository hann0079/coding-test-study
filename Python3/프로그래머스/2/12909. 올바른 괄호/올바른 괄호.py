def solution(s):
    answer = True
    n = 0
    for t in s:
        if t == ')':
            n -= 1
        elif t == '(':
            n += 1
        if n < 0:
            return False
    return answer if not n else False