l = [int(input()) for _ in range(9)]
l.sort()


def backtrack(start, ans):
    if len(ans) == 7:
        if sum(ans) == 100:
            return ans
        return None
    for i in range(start, 9):
        ans.append(l[i])
        result = backtrack(i + 1, ans)
        if result:
            return result
        ans.pop()


result = backtrack(0, [])

for item in result:
    print(item)
