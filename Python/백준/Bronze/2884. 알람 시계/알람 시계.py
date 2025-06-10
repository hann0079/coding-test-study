a, b = map(int, input().split())
if b >= 45:
    b -= 45
else:
    if a == 0:
        a = 24
    a -= 1
    b = 60 - (45 - b)
print(a, b)