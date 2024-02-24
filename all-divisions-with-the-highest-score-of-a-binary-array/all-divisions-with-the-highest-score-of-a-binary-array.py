class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        res_dict = {'max': []}
        i_left = 0
        i_right = nums.count(1)
        N = len(nums)
        for i in range(N+1):
            if i == 0:
                ones_count = i_right
                res_dict['max'].append([i, ones_count])
            else:
                if nums[i-1] == 0:
                    i_left += 1
                else:
                    i_right -= 1

                s = i_left + i_right
                max = res_dict['max'][0]

                if s > max[1]:
                    res_dict['max'] = [[i, s]]
                if s == max[1]:
                    res_dict['max'].append([i, s])

        return [x[0] for x in res_dict['max']]
