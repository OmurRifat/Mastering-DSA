# Solving using a hash map. We create a hash map that maps each Roman numeral to its integer value. We then iterate through the string, and for each character, we check if the previous character has a smaller value than the current character. If it does, we subtract the previous value from the total and add the current value. If it doesn't, we simply add the current value to the total.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        previous_value = 0

        for char in s:
            current_value = roman_numerals[char]
            if previous_value < current_value:
                total += current_value - 2 * previous_value
            else:
                total += current_value
            previous_value = current_value
        return total
    

# Solving using string manipulation. We iterate through the string, and for each character, we check if the next character has a larger value than the current character. If it does, we subtract the current value from the total. If it doesn't, we simply add the current value to the total.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            current_value = roman_numerals[s[i]]
            if i + 1 < len(s) and current_value < roman_numerals[s[i + 1]]:
                total -= current_value
            else:
                total += current_value
        return total
    