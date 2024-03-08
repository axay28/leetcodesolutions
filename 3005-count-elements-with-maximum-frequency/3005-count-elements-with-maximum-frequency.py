class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqmap=collections.Counter(nums)
        x=0
        max_freq=max(freqmap.values())
        for freq in freqmap.values():
            if freq==max_freq:
                x+=freq
        return x
        # return sum(freq for freq in freqmap.values() if freq==max_freq )
        
        