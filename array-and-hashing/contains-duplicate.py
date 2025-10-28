class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ###### solution 1
        # set_nums = set(nums)
        # return len(set_nums) != len(nums)

        
        ###### solution 2
        num_dict = {}
        i = 0

        while i < len(nums):
            if (nums[i] in num_dict.keys()) == False:
                num_dict[nums[i]] = 1
            else:
                num_dict.update({nums[i]: num_dict.get(nums[i]) + 1 })
            i+=1
        
        for x in num_dict:
            if num_dict[x] > 1:
                return True
        
        return False