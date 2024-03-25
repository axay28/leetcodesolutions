class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        count = Counter(nums)
        for k, v in count.items():
            if v > 1: 
                result.append(k)

        return result
        