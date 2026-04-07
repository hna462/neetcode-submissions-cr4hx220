class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        freq = defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1
            while (i-l+1)-(max(freq.values()))>k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)
        return res