class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the topmost element if the stack is not empty
                # Otherwise, assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match, return false
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
        
        # In the end, the stack should be empty if valid
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))      # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]")) 







    



  

