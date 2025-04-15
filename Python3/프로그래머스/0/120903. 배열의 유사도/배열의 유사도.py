def solution(s1, s2):
    answer = 0
    for item1 in s1:
        for item2 in s2:
            if item1 == item2:
                answer += 1
    return answer