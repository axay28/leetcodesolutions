class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqmap=collections.Counter(nums)
        max_freq=max(freqmap.values())
        return sum(freq for freq in freqmap.values() if freq==max_freq )
        
        