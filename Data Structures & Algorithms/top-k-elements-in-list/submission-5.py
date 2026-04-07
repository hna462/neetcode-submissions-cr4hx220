class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        for x,y in freq.items():
            buckets[y].append(x)
        ans = []
        for i in range(len(nums), -1,-1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans
