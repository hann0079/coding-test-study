N, L, H = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
length = len(nums)
avg = (sum(nums[L:length-H])) / (length-L-H)
print(avg)