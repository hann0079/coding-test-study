def solution(arr, divisor):
    answer = [ v for v in arr if v % divisor == 0]
    return sorted(answer) if answer else [-1]