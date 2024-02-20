class Solution:
    def rearrangearray(nums: list[int]):
        ans = []
        N = len(nums)
        neg_vals = [x for x in nums if x < 0]
        pos_vals = [x for x in nums if x > 0]

        for i in range(N//2):
            ans.append(pos_vals[i])
            ans.append(neg_vals[i])

        return ans

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(Solution.rearrangearray(nums))