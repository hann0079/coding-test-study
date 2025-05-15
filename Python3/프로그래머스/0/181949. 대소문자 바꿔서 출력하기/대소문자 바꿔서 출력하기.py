str = input()
result = ''
for s in str:
    if s.isupper():
        result += s.lower()
    else:
        result += s.upper()
print(result)