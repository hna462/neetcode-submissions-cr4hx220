class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        mp = {}
        for r, le in enumerate(s):
            if le in mp:
                l = max(l, mp[le]+1)
            mp[le] = r
            res = max(res, r-l+1)
        return res