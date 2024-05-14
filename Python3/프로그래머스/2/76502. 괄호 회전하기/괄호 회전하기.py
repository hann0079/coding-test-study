def solution(s):
    answer = 0
    opens = ['[', '(', '{']
    closes = [']', ')', '}']
    valid = True 
    have_open = False
    
    for i in range(len(s)):
        curs = s[i:] + s[:i]
        stack = []
        for cur in curs:
            if cur in opens:
                stack.append(cur)
                have_open = True
            elif stack:
                idx = closes.index(cur)
                if stack.pop() != opens[idx]:
                    valid = False 
        if valid and not stack and have_open:
            answer += 1

    return answer