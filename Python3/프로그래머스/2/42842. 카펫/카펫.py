def solution(brown, yellow):
    s = yellow + brown
    for w in range(s-1, 0, -1):
        h = s // w
        ys = (w - 2) * (h - 2)
        bs = s - ys
        if ys == yellow and bs == brown:
            return [w, h]