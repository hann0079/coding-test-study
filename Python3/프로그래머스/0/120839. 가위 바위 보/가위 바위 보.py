def solution(rsp):
    answer = ''
    win = {'2':'0', '0':'5', '5':'2'}
    for r in rsp:
        answer += win[r]
    return answer

