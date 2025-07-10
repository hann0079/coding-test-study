import sys
input = sys.stdin.readline

left = list(input().strip())
right = []

n = int(input())
for _ in range(n):
    cmd = input().strip()
    if cmd == 'L' and left:
        right.append(left.pop())
    elif cmd == 'D' and right:
        left.append(right.pop())
    elif cmd == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[2])

print(''.join(left + right[::-1]))