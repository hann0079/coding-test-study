import sys
n = int(input())
stack = []
for _ in range(n):
    cur = sys.stdin.readline().split()
    if len(cur)== 2:
        stack.append(cur[1])
    elif cur[0] == "pop":
        if len(stack) == 0:
            print(-1)
            continue
        print(stack.pop())
    elif cur[0] == "size":
        print(len(stack))
    elif cur[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    else: # top
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])