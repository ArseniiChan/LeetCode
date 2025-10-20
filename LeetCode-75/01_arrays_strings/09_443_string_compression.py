"""
Problem: String Compression
Difficulty: Medium
Category: String / Two Pointers
LeetCode Link: https://leetcode.com/problems/string-compression/

Approach (UMPIRE):
- Understand:
  Given an array of characters, compress it in-place by replacing consecutive repeated characters with the character followed by its count (if count > 1). Counts >= 10 must be split into separate digit characters. Return the new length of the compressed array.

- Match:
  This is a classic two-pointer problem: one pointer reads groups of characters, another writes the compressed result back into the array. String-to-digit conversion is needed for counts.

- Plan:
  1. Use a read pointer `i` to traverse the array and identify consecutive groups.
  2. For each group, record the character and count.
  3. Use a write pointer `write` to overwrite the array:
     - Always write the character.
     - If count > 1, convert count to string and write each digit.
  4. Return the final `write` index as the new length.

- Implement:
  See code below.

- Review:
  The algorithm correctly handles single characters, multi-digit counts (e.g., 12 → '1','2'), and modifies the array in-place without extra storage beyond a few variables.

- Evaluate:
  The solution is optimal: it makes one pass through the array and uses only constant extra space.

Time Complexity: O(n) — each character is read once and written once.
Space Complexity: O(1) — only a few integer variables and temporary string for digits (digits of a number ≤ 2000 have at most 4 characters, so still constant).
"""

class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        write = 0
        n = len(chars)
        
        while i < n:
            curr_char = chars[i]
            count = 0
            # Count consecutive occurrences
            while i < n and chars[i] == curr_char:
                count += 1
                i += 1
            
            # Write the character
            chars[write] = curr_char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    
    chars1 = ["a","a","b","b","c","c","c"]
    length1 = solution.compress(chars1)
    print(length1, chars1[:length1])  # 6 ['a', '2', 'b', '2', 'c', '3']
    
    chars2 = ["a"]
    length2 = solution.compress(chars2)
    print(length2, chars2[:length2])  # 1 ['a']
    
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    length3 = solution.compress(chars3)
    print(length3, chars3[:length3])  # 4 ['a', 'b', '1', '2']