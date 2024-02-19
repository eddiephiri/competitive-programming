class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = abs(len(nums)//3)
        ans = []
        c = Counter(nums)

        for k in c.keys():
            if c[k] > t:
                ans.append(k)
        
        return ans