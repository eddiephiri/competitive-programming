class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        shortest_str = min(strs, key=len)
        strs.remove(shortest_str)

        if shortest_str == "":
            return common_prefix
        if len(strs) == 0:
            return shortest_str

        for c, i in zip(shortest_str, range(len(shortest_str))):
            for s in strs:
                if s[i] != c:
                    return common_prefix
            common_prefix += c
            
        return common_prefix