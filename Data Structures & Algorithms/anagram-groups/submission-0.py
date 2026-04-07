class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            key = [0]*26
            for l in s:
                key[ord(l)-ord('a')]+=1
            if tuple(key) in hmap:
                hmap[tuple(key)].append(s)
            else:
                hmap[tuple(key)] = [s]
        return list(hmap.values())