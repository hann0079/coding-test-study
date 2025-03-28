from collections import deque
def solution(progresses, speeds):
    #✅ 진도 배열의 값이 들어간 큐를 생성한다.
    q = deque(progresses)
    #✅ 속도 배열의 값이 들어간 큐를 생성한다.
    s = deque(speeds)
    #✅ 정답을 저장할 빈 리스트를 만든다.
    answer = []
    #✅ 진도(속도) 큐에 값이 있는 동안 반복한다.
    while q:
        #✅ 진도 큐에 속도 큐의 값을 각각 더한다.
        for i in range(len(q)):
            q[i] += s[i]
        #✅ 배포 개수를 저장할 변수를 초기화한다.
        cnt = 0
        #✅ 진도 큐의 front가 100 이상인 동안 반복한다.
        while q and q[0] >= 100:
            #✅ 진도 큐와 속도 큐에서 값을 꺼낸다.
            q.popleft()
            s.popleft()
            #✅ count 변수를 1 증가한다.
            cnt += 1
        #✅ count 변수의 값이 0이 아니라면 정답 리스트에 추가한다.
        if cnt:
            answer.append(cnt)
    
    return answer