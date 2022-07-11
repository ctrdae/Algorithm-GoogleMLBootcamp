class Solution(object):
    def isPalindrome(self, s):
        pal = []
        pal_str = ""
        for char in s:
            if char.isalnum() == True:
                pal.append(char.lower())
        pal_str = pal_str.join(pal)
        pal_reversed = "".join(reversed(pal_str))
        if pal_str == pal_reversed:
            return True
        else:
            return False
