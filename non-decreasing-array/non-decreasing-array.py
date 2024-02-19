class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for idx, num in enumerate(nums):
            if idx == n-1:
                return True

            if nums[idx+1] < nums[idx]:
                if idx != 0:
                    if count == 1:
                        return False
                    if nums[idx+1] < nums[idx-1]:
                        nums[idx+1] = nums[idx] + 1
                        count += 1
                    else:
                        nums[idx] = nums[idx+1]
                        count += 1
                else:
                    nums[idx] = nums[idx+1]
                    count += 1
