class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for a in arr:
            if a in freq:
                freq[a]+=1
            else:
                freq[a]=1
        seen_freq={}
        for f in freq.values():
            if f in seen_freq:
                return False
            seen_freq[f] = True
        return True