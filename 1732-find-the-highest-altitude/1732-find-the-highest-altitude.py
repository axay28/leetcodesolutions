class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        highest=curr
        for g in gain:
            curr+=g
            highest=max(highest,curr)
        return highest
        