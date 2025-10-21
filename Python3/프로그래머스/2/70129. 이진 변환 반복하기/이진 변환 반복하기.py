def solution(s):
    answer = [0, 0]
    while s != "1":
        len_of_ones = 0
        for char in s:
            if char == '0':
                answer[1] += 1
            else:
                len_of_ones += 1
        binary_s = ""
        while len_of_ones > 0:
            binary_s += str(len_of_ones % 2)
            len_of_ones //= 2
        s = binary_s[::-1]
        answer[0] += 1
    return answer