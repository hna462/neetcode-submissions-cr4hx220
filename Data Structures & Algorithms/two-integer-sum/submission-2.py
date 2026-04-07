class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            hmap[n] = i
        for i, n in enumerate(nums):
            if (target-n in hmap) and (hmap[target-n] != i):
                return [i, hmap[target-n]]