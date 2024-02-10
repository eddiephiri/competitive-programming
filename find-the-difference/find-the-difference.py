class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t

        for x in t:
            if x not in s:
                return x
            if s.count(x) != t.count(x):
                return x

        return s[0]
