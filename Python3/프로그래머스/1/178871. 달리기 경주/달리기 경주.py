def solution(players, callings):
    answer = players
    ip = {}
    for i, p in enumerate(players):
        ip[p] = i
    for c in callings:
        cur = ip[c]
        answer[cur], answer[cur-1] = answer[cur-1], answer[cur]
        ip[answer[cur]], ip[answer[cur-1]] = ip[answer[cur-1]], ip[answer[cur]]
    return answer