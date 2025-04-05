# 입력 받기
import sys
input = sys.stdin.read  # 빠른 입력
data = input().split()

n = int(data[0])
scores = list(map(int, data[1:]))

# 점수별 빈도 카운트 (0 ~ 75)
count = [0] * 76
for score in scores:
    count[score] += 1

# 높은 점수부터 탐색하며 서로 다른 점수 카운트
distinct = 0
for score in range(75, -1, -1):
    if count[score] > 0:
        distinct += 1
        if distinct == 3:
            print(score, count[score])
            break
