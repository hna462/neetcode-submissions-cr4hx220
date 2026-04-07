from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s)!=len(t):
            return False
        for l in s:
            count[l] = count.get(l, 0) + 1
        for l in t:
            count[l] = count.get(l, 0) - 1
        return not any(count.values())

