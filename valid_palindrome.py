class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch_clear = "" 

        for char in s:
            if ch_clear.isalnum():
                ch_clear += char.lower()
        return ch_clear == ch_clear[::-1]