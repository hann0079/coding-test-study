from collections import Counter

def solution(k, tangerine):
    count_map = Counter(tangerine)
    frequencies = list(count_map.values())
    frequencies.sort(reverse=True)
    tangerines_packed = 0  
    types_count = 0
    for freq in frequencies:
        tangerines_packed += freq
        types_count += 1
        if tangerines_packed >= k:
            return types_count
    return types_count