class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        lower_num = (num - 3) // 3
        mid_num = lower_num + 1
        upper_num = lower_num + 2
        consec_sum = lower_num + mid_num + upper_num

        if consec_sum == num:
            return [lower_num, mid_num, upper_num]
        else:
            return []
