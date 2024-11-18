nums = [int(input()) for _ in range(10)]

s = set()
for num in nums:
    s.add(num%42)

print(len(s))