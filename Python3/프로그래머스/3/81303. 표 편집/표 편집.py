def solution(n, k, cmd):
    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n)]
    down[n - 1] = -1

    deleted = []

    for c in cmd:
        if c[0] == "U":
            x = int(c.split()[1])
            for _ in range(x):
                k = up[k]

        elif c[0] == "D":
            x = int(c.split()[1])
            for _ in range(x):
                k = down[k]

        elif c[0] == "C":
            deleted.append((k, up[k], down[k]))

            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != -1:
                up[down[k]] = up[k]

            k = down[k] if down[k] != -1 else up[k]

        elif c[0] == "Z":
            cur, prev, next = deleted.pop()
            if prev != -1:
                down[prev] = cur
            if next != -1:
                up[next] = cur

    answer = ['O'] * n
    for row, _, _ in deleted:
        answer[row] = 'X'

    return ''.join(answer)