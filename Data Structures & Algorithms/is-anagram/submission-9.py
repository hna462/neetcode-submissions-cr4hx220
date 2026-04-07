from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            count[s[i]]+=1
            count[t[i]]-=1
        return not any(count.values())

