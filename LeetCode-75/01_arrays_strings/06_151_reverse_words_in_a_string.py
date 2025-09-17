"""
Problem: Reverse Words in a String
Difficulty: Medium
Category: String
LeetCode Link: https://leetcode.com/problems/reverse-words-in-a-string/

Approach (UMPIRE):
- Understand: Need to reverse word order, handle multiple/leading/trailing spaces
- Match: String manipulation - split, reverse, join pattern
- Plan: 1) Split string into words (handles spaces automatically)
         2) Reverse the order of words 
         3) Join words back with single spaces
- Implement: Use built-in string methods for clean solution
- Review: Works for all test cases, handles edge cases with spaces
- Evaluate: Could use stack approach, but this is more direct and readable

Time Complexity: O(n) - where n is length of string (split + reverse + join)
Space Complexity: O(n) - storing the words list and result string
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split by whitespace, removes extra spaces
        reversed_words = list(reversed(words))  # Reverse order of words
        return " ".join(reversed_words)  # Join with single spaces


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))  # "blue is sky the"
    print(solution.reverseWords("  hello world  "))  # "world hello"
    print(solution.reverseWords("a good   example"))  # "example good a"