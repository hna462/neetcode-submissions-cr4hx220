class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxh = 0
        # two pointers to calc max height, multiply min(heights[l], heights[r]) with (r-l)
        # compeare temp calc with maxh and store it, return maxh
        while l<r:
            currh = min(heights[l], heights[r]) * (r-l)
            maxh = max(currh, maxh)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxh