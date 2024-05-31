def performselectionsort(nums):
    n = len(nums)
    fixthisindex =n-1
    while fixthisindex > 0:
        for index in range(fixthisindex):
            if nums[index] > nums[index + 1]:
                temp = nums[index]
                nums[index] = nums[index + 1]
                nums[index + 1] =temp
        print(nums)
        fixthisindex -= 1
nums = [10,4,6,23,9]
print("before sorting :", nums)
performselectionsort(nums)
print("after sorting:",nums)
