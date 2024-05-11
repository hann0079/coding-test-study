def solution(answers):
    answer = []
    length = len(answers)
    one = [1, 2, 3, 4, 5] * length
    two = [2,1,2,3,2,4,2,5] * length
    three = [3,3,1,1,2,2,4,4,5,5] * length
    one_cnt, two_cnt, three_cnt = 0, 0, 0
    for i in range(length):
        if answers[i] == one[i]:
            one_cnt += 1
        if answers[i] == two[i]:
            two_cnt += 1
        if answers[i] == three[i]:
            three_cnt += 1
    max_value = max(one_cnt, two_cnt, three_cnt)
    if max_value == one_cnt:
        answer.append(1)
    if max_value == two_cnt:
        answer.append(2)
    if max_value == three_cnt:
        answer.append(3)
    return answer