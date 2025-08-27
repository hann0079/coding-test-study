from collections import deque
def solution(arr):
    q = deque(arr)
    answer = [q.popleft()]
    while q:
        val = q.popleft()
        if answer[-1] != val:
            answer.append(val)
    return answer