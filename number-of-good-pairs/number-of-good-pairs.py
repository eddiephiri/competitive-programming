class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        if nums == [] or len(nums) == 1:
            return 0

        for _ in range(len(nums) - 1):
            num = nums.pop(0)
            good_pairs += nums.count(num)

        return good_pairs
    