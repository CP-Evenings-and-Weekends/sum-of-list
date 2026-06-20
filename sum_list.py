def sum_of_list (nums, i=0):
    if i == len(nums):
        return 0
    return nums[i] + sum_of_list (nums, i+1)

print(sum_of_list([]))           # 0
print(sum_of_list([5]))          # 5
print(sum_of_list([1, 2, 3]))    # 6
print(sum_of_list([-1, 1, -1]))  # -1