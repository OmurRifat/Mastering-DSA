# Solving using string manipulation. We convert the integer to a string, and then check if the string is the same as its reverse. If they are the same, then the integer is a palindrome.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        input_str = str(x)
        return input_str == input_str[::-1]
    
# Solving using mathematical manipulation. We reverse the integer by extracting its digits and constructing a new integer. If the reversed integer is the same as the original integer, then it is a palindrome. We also need to handle negative integers, which cannot be palindromes.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        input_int = x
        if input_int < 0:
            return False
        else:
            reversed_int = 0
            while input_int > 0:
                last_digit = input_int % 10
                reversed_int = reversed_int * 10 + last_digit
                input_int //= 10
            return x == reversed_int