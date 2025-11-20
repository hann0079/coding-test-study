def solution(targets):
    answer = 0
    t = targets
    t.sort(key=lambda x:x[1])
    end = 0
    for c in t:
        if c[0] >= end:
            answer += 1
            end = c[1]
    return answer