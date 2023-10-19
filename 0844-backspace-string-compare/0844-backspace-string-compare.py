class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_1=[]
        t_1=[]
        for i in range(len(s)):
            if s[i]=="#":
                if s_1:
                    s_1.pop()
            else:
                s_1.append(s[i])
        for i in range(len(t)):
            if t[i]=="#":
                if t_1:
                    t_1.pop()
            else:
                t_1.append(t[i])
        return t_1==s_1
        
        
        