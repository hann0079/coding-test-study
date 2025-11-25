def solution(info, n, m):
    # dp[b] = B의 누적 흔적이 b일 때, A의 최소 누적 흔적
    # B가 m 이상이면 잡히므로 dp 배열의 크기는 m으로 설정 (0 ~ m-1)
    INF = float('inf')
    dp = [INF] * m
    
    # 초기 상태: 아무것도 훔치지 않았을 때 A=0, B=0
    dp[0] = 0
    
    for trace_a, trace_b in info:
        # 이번 물건을 처리한 후의 상태를 저장할 임시 배열
        next_dp = [INF] * m
        
        for b in range(m):
            # 도달 불가능한 상태는 건너뜀
            if dp[b] == INF:
                continue
            
            current_a_trace = dp[b]
            
            # Case 1: A 도둑이 훔치는 경우
            # 조건: A의 누적 흔적이 n보다 작아야 함
            if current_a_trace + trace_a < n:
                # B의 흔적(b)은 그대로, A의 흔적만 증가
                next_dp[b] = min(next_dp[b], current_a_trace + trace_a)
            
            # Case 2: B 도둑이 훔치는 경우
            # 조건: B의 누적 흔적이 m보다 작아야 함
            if b + trace_b < m:
                # A의 흔적은 그대로, B의 흔적(인덱스)만 증가
                next_dp[b + trace_b] = min(next_dp[b + trace_b], current_a_trace)
        
        # dp 배열 업데이트
        dp = next_dp

    # 모든 물건을 훔친 후, dp 배열에서 최솟값 찾기
    answer = min(dp)
    
    # 만약 최솟값이 여전히 INF라면, 불가능한 경우임
    return answer if answer != INF else -1