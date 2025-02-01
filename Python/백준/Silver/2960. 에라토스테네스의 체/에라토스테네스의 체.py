N, K = map(int, input().split())

def find_prime(n, k):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    cnt = 0
    for i in range(n+1):
        if is_prime[i] == True:
            for j in range(i, n+1, i):
                if is_prime[j] == False:
                    continue

                is_prime[j] = False
                cnt += 1

                if cnt == k:                    
                    return j 

print(find_prime(N, K))