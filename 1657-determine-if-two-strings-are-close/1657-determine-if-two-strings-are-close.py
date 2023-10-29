class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        if set(word1)==set(word2) and sorted(list(c1.values())) == sorted(list(c2.values())):
            return True
        return False
        