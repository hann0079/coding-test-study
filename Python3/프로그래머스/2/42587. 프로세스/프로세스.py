from collections import deque
def solution(priorities, location):
    answer = []
    # 큐에 인덱스(프로세스번호), 우선순위 저장
    queue = deque()
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    # 큐에 값이 있는 동안
    while queue:
        new = queue.popleft()
        if any((new[1]<q[1] for q in queue)):
            queue.append(new)
        else:
            answer.append(new)
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1