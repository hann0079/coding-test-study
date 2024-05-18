from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    cnt = 0
    
    for _ in range(3 * len(queue1)):
        if sum1 > sum2:
            v = q1.popleft()
            sum1 -= v
            q2.append(v)
            sum2 += v
            cnt += 1
        elif sum1 < sum2:
            v = q2.popleft()
            sum2 -= v
            q1.append(v)
            sum1 += v
            cnt += 1
        else:
            return cnt
    
    return -1
