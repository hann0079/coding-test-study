from collections import deque


def solution(progresses, speeds):
    answer = []

    queue = deque(progresses)
    length = len(progresses)

    cnt = 1
    for i in range(length):
        pre_cnt = cnt
        while progresses[i] + (speeds[i] * cnt) < 100:
            cnt += 1
        next_cnt = cnt
        if pre_cnt != next_cnt:
            answer.append(1)
        else:
            answer[-1] += 1
        queue.popleft()

    return answer