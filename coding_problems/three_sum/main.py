
#This is the sume of three problem

#where we have some dictionary or list nums, where we need to find three elements that equal the target
# ex1:


def three_sum(nums, target):

    nums.sort()

    for i in range(0, len(nums)-2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                return True
                
            elif triplet < target:
                low += 1
            
            else:
                high -= 1
    
        return False