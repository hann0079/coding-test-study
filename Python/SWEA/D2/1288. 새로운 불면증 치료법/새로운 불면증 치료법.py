# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    flags = {str(n): False for n in range(10)}
    num = 0
    while not all(flags.values()):
        num += 1
        cur = str(num * N)
        for c in cur:
            if not flags[c]:
                flags[c] = True
    print(f"#{test_case} {num*N}")
    # ///////////////////////////////////////////////////////////////////////////////////
