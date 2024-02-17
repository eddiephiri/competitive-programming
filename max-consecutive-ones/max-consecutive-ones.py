class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = []
        count = 0

        if 1 not in nums:
            return 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums)-1:
                    counts.append(count)
            elif count > 0:
                counts.append(count)
                count = 0
        
        return max(counts)