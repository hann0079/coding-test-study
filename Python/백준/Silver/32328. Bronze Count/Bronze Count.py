n = int(input())
scores = [int(input()) for _ in range(n)]

# 1. 점수 정렬
unique_scores = sorted(set(scores), reverse=True)

# 2. 세 번째 점수 (Bronze)
bronze_score = unique_scores[2]

# 3. bronze 점수를 받은 사람 수 세기
count = scores.count(bronze_score)

print(bronze_score, count)
