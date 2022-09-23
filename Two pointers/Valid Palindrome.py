# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() is False:  # isalnum()
                l += 1
                continue
            if s[r].isalnum() is False:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():  # lower()
                return False
            else:
                l += 1
                r -= 1
        return True
