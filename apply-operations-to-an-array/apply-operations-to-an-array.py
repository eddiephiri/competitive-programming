class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        left = [x for x in nums if x > 0]
        right = [y for y in nums if y == 0]
        
        return left + right
