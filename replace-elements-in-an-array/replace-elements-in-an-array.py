class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hm = {num: i for i, num in enumerate(nums)}

        for i, n in operations:
            nums[hm[i]] = n
            hm[n] = hm[i]
            del hm[i]

        return nums