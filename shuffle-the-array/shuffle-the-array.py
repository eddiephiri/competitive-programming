class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ptr1 = 0
        ptr2 = n
        res = []

        for _ in range(n):
            res.append(nums[ptr1])
            res.append(nums[ptr2])
            ptr1 += 1
            ptr2 += 1

        return res