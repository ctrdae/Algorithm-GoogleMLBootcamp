class Solution(object):
    def isPalindrome(self, s):
        pal = ""
        for char in s:
            if isinstance(char, str) == True:
                pal.append(char.lower())
        pal_reversed = "".join(reversed(pal))
        if pal == pal_reversed:
            return True
        else:
            return False
