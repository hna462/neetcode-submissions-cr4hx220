class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {')':'(', '}':'{', ']':'['}
        stack = []
        for p in s:
            if p in pmap:
                if not stack or pmap[p] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        return not stack