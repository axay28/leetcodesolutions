class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict={}
        for s in strs:
            sorted_string=" ".join(sorted(s))
            if sorted_string not in mydict:
                mydict[sorted_string]=[]
            mydict[sorted_string].append(s)
        return mydict.values()
                
        