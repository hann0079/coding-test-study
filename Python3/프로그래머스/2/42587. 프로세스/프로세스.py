from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((i , priorities[i]))
    while q:
        if q[0][1] >= max(q, key=lambda x:x[1])[1]:
            m = q.popleft()
            answer += 1
            if location == m[0]:
                return answer
        else:
            q.append(q.popleft())

    return answer