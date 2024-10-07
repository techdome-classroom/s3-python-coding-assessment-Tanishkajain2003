class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize the total result
        total = 0
        
        # Iterate through the Roman numeral string
        for i in range(len(s)):
            # If the current Roman numeral is smaller than the next one, subtract its value
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                # Otherwise, add its value to the total
                total += roman[s[i]]
        
        return total
    



