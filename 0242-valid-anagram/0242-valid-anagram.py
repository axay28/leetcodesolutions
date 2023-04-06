class Solution(object):
    def isAnagram(self, s, t):
        if s=="" and t== "":
            return False
        if len(set(s))!= len(set(t)) or len(s)!=len(t):
            return False
        for char in set(s):
            s_count=s.count(char)
            t_count=t.count(char)
            if s_count!=t_count:
                return False
        return True
        