def solution(s):
    answer = True
    stack = []
    for p in s:
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                return False
            top = stack.pop()
    if stack:
        return False
    return True
    