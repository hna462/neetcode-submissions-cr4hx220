from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        return not any(count.values())

