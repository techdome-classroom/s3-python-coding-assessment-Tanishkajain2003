class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize the result
        result = 0
        
        # Iterate over the string
        for i in range(len(s)):
            # If the current value is less than the next value, subtract it
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                # Otherwise, add the value
                result += roman[s[i]]
                
        return result
        pass







    



  

