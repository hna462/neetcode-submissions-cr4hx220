from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = defaultdict(int)
        tcount = defaultdict(int)
        for l in s:
            scount[l] += 1
        for l in t:
            tcount[l] += 1
        return scount == tcount