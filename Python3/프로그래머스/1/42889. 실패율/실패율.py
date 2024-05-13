def solution(N, stages):
    answer = []
    length = len(stages)
    tmp = dict()
    
    pre = 0
    for i in range(1, N + 1):
        cur_stage = length - pre 
        cnt = stages.count(i)
        cur_fail = cnt / cur_stage if cur_stage != 0 else 0
        pre += cnt
        if cur_fail in tmp:
            tmp[cur_fail].append(i)
        else:
            tmp[cur_fail] = [i]

    ks = sorted(tmp.keys(), reverse=True)
    for k in ks:
        answer.extend(tmp[k])
        
    return answer