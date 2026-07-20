class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)

        if(l1 == l2 and sorted(s) == sorted(t)):
            return True
        else:
            return False