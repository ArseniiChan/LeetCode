class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Convert number to string and handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse digits using string slicing
        rev_str = str(x)[::-1]
        
        # Convert back to integer
        rev_int = int(rev_str) * sign
        
        # Check for overflow
        if rev_int < INT_MIN or rev_int > INT_MAX:
            return 0
        
        return rev_int