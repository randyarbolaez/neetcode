class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        answer = []

        i = 0
        while i < len(nums):
            remaining[target - nums[i]] = i
            i+=1
            
        for j in range(len(nums)):
            if nums[j] in remaining:
                if j != remaining[nums[j]]:
                    answer.append(j)
                    answer.append(remaining[nums[j]])
                    break

        return answer