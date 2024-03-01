class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
        	return []
        if len(nums) == 1:
	        return [nums[0]]
        freq_map=collections.Counter(nums)
        h=[(-freq_map, num) for num, freq in freq_map.items()]
        heapq.heapify(h)
        res = heapq.nlargest(k, freq_map.keys(), key=freq_map.get)
        return res
