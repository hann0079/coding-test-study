N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
length = len(scores)
for i in range(length):
    scores[i] = scores[i]/M*100

print(sum(scores)/length)