class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        result = []
        for i in range(len(positives)):
            result.append(positives[i])
            result.append(negatives[i])
        return result

        