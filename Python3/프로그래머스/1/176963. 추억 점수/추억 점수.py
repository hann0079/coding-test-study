def solution(name, yearning, photo):
    answer = []
    nums = {}
    for n, y in zip(name, yearning):
        nums[n] = y
        
    for p in photo:
        result = 0
        for c in p:
            if c in nums:
                result += nums[c] 
        answer.append(result)
    return answer