class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [x for x in nums if x < pivot]

        for i in range(len(nums)):
            if nums[i] == pivot:
                res.append(nums[i])
        for i in range(len(nums)):
            if nums[i] > pivot:
                res.append(nums[i])

        return res
    