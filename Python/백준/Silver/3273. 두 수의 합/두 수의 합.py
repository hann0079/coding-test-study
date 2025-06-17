len_a = int(input())
a = list(map(int, input().split()))
x = int(input())

left = 0
right = len_a - 1
cnt = 0
a.sort()

while left < right:
  result = a[left] + a[right]
  if result < x:
    left += 1
  elif result > x:
    right -= 1
  else:
    cnt += 1
    left += 1
    right -= 1

print(cnt)