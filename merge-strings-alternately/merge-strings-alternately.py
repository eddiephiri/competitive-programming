class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""

        if "" in [word1, word2]:
            return max([word1, word2], key=len)

        longest_word = max([word1, word2], key=len)
        shortest_word = min([word1, word2], key=len)
        for i in range(len(longest_word)):
            if i > len(shortest_word) - 1:
                new_str += longest_word[i]
            else:
                new_str += word1[i]
                new_str += word2[i]
        
        return new_str