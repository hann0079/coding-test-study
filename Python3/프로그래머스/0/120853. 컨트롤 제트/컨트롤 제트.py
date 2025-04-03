def solution(s):
    stack = []
    sum_ = 0
    # 문자열을 나눠 리스트 만들기
    sl = s.split()
    # 리스트 요소만큼 반복하기
    for item in sl:
        # Z 라면
        if item == "Z":
            # 스택에서 pop
            # 합계에서 minus
            sum_ -= stack.pop()
        # Z가 아니라면 
        else:
            ii = int(item)
            # 스택에 push
            stack.append(ii)
            # 합계에 plus
            sum_ += ii
    return sum_
