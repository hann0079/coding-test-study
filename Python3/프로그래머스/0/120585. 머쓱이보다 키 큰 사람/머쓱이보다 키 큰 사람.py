def solution(array, height):
    cnt = 0
    for value in array:
        if value > height :
            cnt += 1
    return cnt