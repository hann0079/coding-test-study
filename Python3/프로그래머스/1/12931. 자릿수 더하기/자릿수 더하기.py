def solution(n):
    answer = 0
    sn = str(n)
    for i in range(len(sn)):
        answer += int(sn[i])
    return answer