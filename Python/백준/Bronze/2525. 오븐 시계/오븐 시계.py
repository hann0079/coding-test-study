h, m = map(int, input().split())
t = int(input())

q, r = divmod(m+t, 60)
print((h+q) % 24, r)