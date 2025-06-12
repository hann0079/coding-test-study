h, m = map(int, input().split())
t = int(input())

result = m + t 
while result >= 60:
    h += 1
    if h == 24:
        h = 0
    result -= 60

print(h, result)