T = int(input())

for test_case in range(1, T+1):
    R, S = input().split()
    R = int(R)
    result = ""
    for letter in S:
        result += letter*R

    print(result)