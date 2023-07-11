# Kadane's Algorithm

l = list(map(int,input().strip().split()))

maxSum = l[0]
curSum = 0

for n in l:
    curSum = max(curSum, 0)
    curSum += n
    maxSum = max(curSum, maxSum)

print(maxSum)

# Variation: Sliding Window

nums = [4, -1, 2, -7, 3, 5]

maxL, maxR = 0, 0
L = 0
cur = 0
max = nums[0]  # Considering non empty array

for R in range(len(nums)):
    if cur < 0:
        cur = 0
        L = R
    cur += nums[R]
    if cur > max:
        max = cur
        maxL = L
        maxR = R

print([maxL, maxR])
