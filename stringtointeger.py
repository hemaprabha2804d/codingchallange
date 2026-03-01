class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()  # Remove leading spaces
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # Check sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        result = 0
        
        # Convert digits to integer
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        
        # Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result