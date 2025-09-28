def solution(s):
    str = list(map(int, s.split()))
    answer = "%d %d" % (min(str),max(str))
    # answer = f"{min(str), max(str)}"
    # answer = str(min(str)) + " " + str(max(str))
    return answer