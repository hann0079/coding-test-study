T = int(input())

for _ in range(T):
    stack = []
    str = input()
    # 괄호 판별을 위한 반복문
    for c in str:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # stack에 뭐라도 있는 경우
            if stack:
                stack.pop()
            # stack에 아무것도 없는 경우    
            else:
                print("NO")
                break
    else:        
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")     