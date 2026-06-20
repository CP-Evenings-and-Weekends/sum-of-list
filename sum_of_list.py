# define the function
def sum_of_list(nums):
    # check if parameter 'nums' is an empty list since that's the base case
    if nums == []:
        # if true, return 0
        # an empty list has nothing in it, so its sum is 0
        return 0
    else:
        # nums[1:] is slicing "everything except the first element" 
        # if nums = [1, 2, 3], then nums[1:] is [2, 3]
        return nums[0] + sum_of_list(nums[1:])