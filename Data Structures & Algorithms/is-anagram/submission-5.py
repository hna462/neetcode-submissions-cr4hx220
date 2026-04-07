from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for l in s:
            count[ord(l)-ord('a')]+=1
        for l in t:
            count[ord(l)-ord('a')]-=1
        return count == [0]*26