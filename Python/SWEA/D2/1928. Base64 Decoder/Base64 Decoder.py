# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
base = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    encoded = input()
    total = decoded = ''
    for e in encoded:
        total += format(base.index(e), '06b')
    for i in range(0, len(total), 8):
        num = int(total[i:i+8], 2)
        decoded += chr(num)
    print(f"#{test_case} {decoded}")
    # ///////////////////////////////////////////////////////////////////////////////////