import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        print(math.log(n,3))
        print(math.log(n,3) - math.floor(math.log(n,3)))
        if math.log(n,3) - math.floor(math.log(n,3)) >= 0.99999999999999: return True
        return math.log(n,3).is_integer()
    

check = Solution()
result = check.isPowerOfThree(19682)

# print(result)