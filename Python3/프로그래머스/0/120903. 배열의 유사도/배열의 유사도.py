def solution(s1, s2):
    answer = set(s1).intersection(set(s2))
    return len(answer)