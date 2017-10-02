class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        DEBUG_FLAG = True
        num_dict = {}
        
        if DEBUG_FLAG == True:
            print("String = {}".format(nums))
            print("Target = {}".format(target))

        
        for index, num in enumerate(nums):
            if DEBUG_FLAG == True:
                print("Index = {}, Num = {}".format(index, num))
            num_dict[num] = index   
    
        for index, num in enumerate(nums):
            num_2 = target - num
            if num_2 in num_dict and num_2 != num:   
                return [index, num_dict[num_2]]
