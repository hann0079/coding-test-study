def solution(s):
    stack = []
    # 문자열을 나눠 리스트 만들기
    # 리스트 요소만큼 반복하기
    for item in  s.split():
        # Z 라면
        if item == "Z":
            # 스택에서 pop
            stack.pop()
        # Z가 아니라면 
        else:
            ii = int(item)
            # 스택에 push
            stack.append(ii)
    return sum(stack)
