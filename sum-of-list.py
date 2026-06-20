def sum_of_list(nums): #create a function
    if nums == []: #is the list empty?[]
        return 0 #if the list is empty give back 0
    else: #otherwise
        return nums[0] + sum_of_list(nums[1:])
# nums[0] = grab the first number in the list
# nums [1:] = everything after the first list
# sum_of_list(...) = call ourselves again with the smaller list
    
print(sum_of_list([5])) #5
print(sum_of_list([8, 6, 4])) # 18