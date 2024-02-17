class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_str1 = "".join(word1)
        word_str2 = "".join(word2)
        
        return word_str1 == word_str2