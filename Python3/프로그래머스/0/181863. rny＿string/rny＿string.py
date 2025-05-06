def solution(rny_string):
    answer = ''
    for s in rny_string:
        if s == "m":
            s = "rn"
        answer += s
    return answer