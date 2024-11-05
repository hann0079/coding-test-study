# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
primes = [2, 3, 5, 7, 11]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    counts = {p: 0 for p in primes}

    for p in primes:
        while N % p == 0:
            counts[p] += 1
            N //= p

    result = " ".join(str(counts[p]) for p in primes)
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////