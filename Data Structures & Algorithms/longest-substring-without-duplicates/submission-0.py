class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength, l = 0, 0
        lmap = {}
        for i, letter in enumerate(s):
            if letter in lmap and lmap[letter] >= l:
                l = lmap[letter] + 1
            lmap[letter] = i
            maxlength = max(maxlength, i-l+1)
        return maxlength