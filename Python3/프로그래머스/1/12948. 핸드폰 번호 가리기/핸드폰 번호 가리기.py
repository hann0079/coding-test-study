def solution(phone_number):
    answer = ''
    space = len(phone_number) - 4
    answer += '*' * space
    return answer + phone_number[space:]