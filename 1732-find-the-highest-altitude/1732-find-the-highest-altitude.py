class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        nowh=0
        maxh=0
        for x in gain:
            nowh+=x
            maxh=max(maxh,nowh)
        return maxh
        