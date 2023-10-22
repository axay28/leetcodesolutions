class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if 'Inf' in s or 'inf' in s or 'nan' in s:
                return False
            num = float(s)
            return True
        except:
            return False