l = list()
length = 9
for _ in range(length):
    l.append(int(input()))
    l.sort()


def backtrack(start, ans):
    if len(ans) == 7:
        return
    for i in range(start, length):
        ans.append(l[i])
        backtrack(i + 1, ans)
        if sum(ans) == 100:
            result.append(ans[:])
        ans.pop()


result = []
backtrack(0, [])

for item in result[0]:
    print(item)