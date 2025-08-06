nums = [3,2,4]
target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        sum = nums[i] + nums[j]
        if sum == target:
            print(f"[{i},{j}]")