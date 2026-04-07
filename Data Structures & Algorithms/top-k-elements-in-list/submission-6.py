class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for v,f in freq.items():
            heapq.heappush(heap, (f, v))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for f, v in heap:
            ans.append(v)
        return ans
            
