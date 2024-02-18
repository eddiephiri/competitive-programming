class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counter = Counter(nums)
        counts = list(num_counter.values())

        if max(counts) > 1:
            return True
        return False