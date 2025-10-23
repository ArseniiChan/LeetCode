"""
Problem: Move Zeroes
Difficulty: Easy
Category: Array
LeetCode Link: https://leetcode.com/problems/move-zeroes/

Approach (UMPIRE):
- Understand:
  Given an integer array `nums`, move all 0's to the end while maintaining the relative order of non-zero elements.
  Must modify the array in-place; no extra space allowed (except a few variables).

- Match:
  Two-pointer technique — one to track the position to place the next non-zero (write pointer), another to scan the array (read pointer).

- Plan:
  1. Initialize a `left` pointer at 0 to track where the next non-zero should be placed.
  2. Iterate through the array with a `right` pointer (from 0 to end):
     - If `nums[right]` is non-zero, copy it to `nums[left]` and increment `left`.
  3. After processing all elements, fill all positions from `left` to the end with 0s.

- Implement:
  Use a for-loop for reading, then a while-loop (or for-loop) to zero out the tail.

- Review:
  Test with edge cases: all zeros, no zeros, single element, zeros at start/end.

- Evaluate:
  This approach ensures non-zero order is preserved and zeros are correctly moved to the end with minimal operations.

Time Complexity: O(n) — we traverse the array twice (once for non-zeros, once for zeros), but still linear.
Space Complexity: O(1) — only a few extra variables used; in-place modification.
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        n = len(nums)
        
        # Move all non-zero elements to the front
        for right in range(n):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        
        # Fill the remaining positions with zeros
        while left < n:
            nums[left] = 0
            left += 1


if __name__ == "__main__":
    # Example test case
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)  # Expected output: [1, 3, 12, 0, 0]