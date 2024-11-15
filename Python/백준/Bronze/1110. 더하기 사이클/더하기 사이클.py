N = int(input())
cnt = 0
new = N
while True:
    left = new // 10
    right = new % 10
    result = left + right
    new = int(str(right) + str(result % 10))
    cnt += 1
    if N == new:
        break
print(cnt)