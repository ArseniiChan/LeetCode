"""
Problem: Greatest Common Divisor of Strings
Difficulty: Easy
Category: Array / String
LeetCode Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/

Approach (UMPIRE):
- Understand: Find the largest string that can divide both input strings by repetition
- Match: Mathematical GCD concept applied to strings + string manipulation
- Plan: 
  1. Quick elimination: if str1+str2 != str2+str1, no common pattern exists
  2. Find GCD of string lengths - this gives us the length of our answer
  3. Extract prefix of that length and return it
- Implement: Use math.gcd and string slicing
- Review: Handles edge cases (no common divisor) and works for all examples
- Evaluate: Clean and efficient solution using mathematical insight

Time Complexity: O(n + m) where n, m are string lengths
Space Complexity: O(n + m) for string concatenation
"""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Quick check: if GCD exists, str1 + str2 == str2 + str1
        # This works because if both strings are made of repeating the same pattern,
        # concatenating them in either order gives the same result
        if str1 + str2 != str2 + str1:
            return ""
        
        # If a common pattern exists, its length must be gcd(len(str1), len(str2))
        gcd_length = gcd(len(str1), len(str2))
        
        # The pattern is the prefix of either string with that length
        return str1[:gcd_length]


if __name__ == "__main__":
    # Test cases
    solution = Solution()
    
    # Example 1
    print(solution.gcdOfStrings("ABCABC", "ABC"))  # Expected: "ABC"
    
    # Example 2  
    print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Expected: "AB"
    
    # Example 3
    print(solution.gcdOfStrings("LEET", "CODE"))  # Expected: ""