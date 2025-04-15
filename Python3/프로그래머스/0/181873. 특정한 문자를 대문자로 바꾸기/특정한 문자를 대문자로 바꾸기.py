def solution(my_string, alp):
    answer = ''
    for s in my_string:
        if s == alp:
            answer += alp.upper()
            continue
        answer += s
    return answer