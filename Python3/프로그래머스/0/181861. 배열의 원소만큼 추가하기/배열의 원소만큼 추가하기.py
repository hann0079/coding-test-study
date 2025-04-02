def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.extend([arr[i]] * arr[i])
    return answer