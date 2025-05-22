def solution(numer1, denom1, numer2, denom2):
    up = numer1*denom2 + numer2*denom1
    down = denom1 * denom2
    for i in range(min(up,down), 0, -1):
        if up % i == 0 and down % i == 0:
            return [up//i, down//i]