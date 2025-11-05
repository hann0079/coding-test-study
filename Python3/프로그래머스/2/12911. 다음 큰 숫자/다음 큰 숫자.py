def solution(n):
    for i in range(n, 1000000):
        answer = ''
        x = i
        while x != 1:
            answer += str(x % 2)
            x //= 2
        if i == n:
            nc = answer.count('1')
        elif nc == answer.count('1'):
            return i