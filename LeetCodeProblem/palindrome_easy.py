class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        input_str = str(x)
        return input_str == input_str[::-1]