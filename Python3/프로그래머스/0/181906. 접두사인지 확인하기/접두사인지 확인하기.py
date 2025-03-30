def solution(my_string, is_prefix):
    return 1 if my_string.startswith(is_prefix) else 0
#     # 부분문자열 문제 - 슬라이싱
#     # 앞에서부터 확인 필요 
#     # prefix의 length를 구해서 그만큼 슬라이싱
#     # prefix가 더 긴 경우 처리 필요
#     l = len(is_prefix)
#     if l > len(my_string):
#         return 0

#     return 1 if my_string[:l] == is_prefix else 0

