def solution(want, number, discount):
    answer = 0
    
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for j in range(len(discount) - 9):
        cur = {}
        for k in range(j, j + 10):
            if discount[k] in dic:
                cur[discount[k]] = cur.get(discount[k], 0) + 1
        if cur == dic:
            answer += 1
            
    return answer