"""
Problem: Reverse Vowels of a String
Difficulty: Easy
Category: String / Two Pointers
LeetCode Link: https://leetcode.com/problems/reverse-vowels-of-a-string/

Approach (UMPIRE):
- Understand: Reverse only the vowels in a string while keeping consonants in their original positions
- Match: Two-pointer technique - converging pointers from both ends
- Plan: Use left/right pointers, skip consonants, swap when both point to vowels
- Implement: Convert to list for mutability, use set for O(1) vowel lookup
- Review: Check edge cases (no vowels, all vowels, single character)
- Evaluate: Efficient single-pass solution with minimal extra space

Time Complexity: O(n) - single pass through string
Space Complexity: O(n) - for converting string to list (strings are immutable in Python)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s_list[left] not in vowels:
                left += 1
            elif s_list[right] not in vowels:
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return ''.join(s_list)


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    print(solution.reverseVowels("IceCreAm"))  # Expected: "AceCreIm"
    print(solution.reverseVowels("leetcode"))  # Expected: "leotcede"