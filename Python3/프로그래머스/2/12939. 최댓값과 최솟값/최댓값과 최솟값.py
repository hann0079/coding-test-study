def solution(s):
    str = list(map(int, s.split()))
    answer = f"{min(str)} {max(str)}"
    return answer