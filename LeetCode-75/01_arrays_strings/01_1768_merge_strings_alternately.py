"""
Problem: 1768. Merge Strings Alternately
Difficulty: Easy
Category: Array / String
LeetCode Link: https://leetcode.com/problems/merge-strings-alternately/

Approach (UMPIRE):
- Understand: Merge two strings by alternating characters from each, starting with word1. 
  If one string is longer, append remaining characters to the end.
- Match: Two pointers pattern - process two inputs simultaneously
- Plan: Use two pointers to track position in each string. Alternate based on result length 
  (even = word1, odd = word2). Handle edge case when one string runs out.
- Implement: See solution below
- Review: Check edge cases (different lengths, empty strings)
- Evaluate: O(m+n) time, O(m+n) space - optimal for this problem

Time Complexity: O(m + n) where m = len(word1), n = len(word2)
Space Complexity: O(m + n) for the result string
"""

class Solution:
    def mergeAlternately(self, word1, word2):
        result = ""
        pointer1, pointer2 = 0, 0
        
        # Continue while either string has characters left
        while pointer1 < len(word1) or pointer2 < len(word2):
            if len(result) % 2 == 0:  # Even length = word1's turn
                if pointer1 < len(word1):
                    result += word1[pointer1]
                    pointer1 += 1
                else:
                    # word1 exhausted, take from word2
                    result += word2[pointer2]
                    pointer2 += 1
            else:  # Odd length = word2's turn
                if pointer2 < len(word2):
                    result += word2[pointer2]
                    pointer2 += 1
                else:
                    # word2 exhausted, take from word1
                    result += word1[pointer1]
                    pointer1 += 1
        
        return result


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    print(solution.mergeAlternately("abc", "pqr"))    # "apbqcr"
    print(solution.mergeAlternately("ab", "pqrs"))    # "apbqrs"
    print(solution.mergeAlternately("abcd", "pq"))    # "apbqcd"