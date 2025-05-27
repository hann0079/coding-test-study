def solution(num_list):
    odd = ""
    even = ""
    for n in num_list:
        if n % 2 != 0:
            odd += str(n)
        else:
            even += str(n)
    return int(odd) + int(even)