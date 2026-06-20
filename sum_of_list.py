def sum_of_list(nums):
    # base case of if the list is empty, it sum is 0
    if len(nums) == 0:
        return 0

    else:
        # takes the first number and add it to sum of the remaining sliced list
        return nums[0] + sum_of_list(nums[1:])


print(sum_of_list([1, 2, 3, 4]))  # 10
print(sum_of_list([]))          # 0
print(sum_of_list([5]))          # 5
print(sum_of_list([1, 2, 3]))    # 6
print(sum_of_list([-1, 1, -1]))  # -1
