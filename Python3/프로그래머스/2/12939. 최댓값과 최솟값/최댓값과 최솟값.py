def solution(s):
    str = list(map(int, s.split()))
    answer = "%d %d" % (min(str),max(str))
    return answer