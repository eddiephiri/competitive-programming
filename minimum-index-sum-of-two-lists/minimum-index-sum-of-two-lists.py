class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = {}
        for i, s in enumerate(list1):
            if s in list2:
                print(list2.index(s))
                ans[s] = i + list2.index(s)

        return [k for k in ans.keys() if ans[k] == min(ans.values())]