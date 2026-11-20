def binary_search(nums, target):     
    start = 0     
    end = len(nums) - 1     
    
    while start <= end:         
        mid = (start + end) // 2         
        if nums[mid] == target:             
            return mid         
        elif nums[mid] < target:             
            start = mid + 1                      
        else:             
            end = mid - 1                           
            
    return -1 

print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))








    
    # target = len(nums) // 2
    # return target

    # while i < len(nums):
    #     if i == target:art
    #         return i
    #     else:
    #         return -1


        