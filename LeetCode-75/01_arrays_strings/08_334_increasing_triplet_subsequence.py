"""
Problem: Increasing Triplet Subsequence
Difficulty: Medium
Category: Array
LeetCode Link: https://leetcode.com/problems/increasing-triplet-subsequence/

Approach (UMPIRE):
- Understand:
  Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. The elements do not need to be consecutive.

- Match:
  This is a classic problem that can be solved with a greedy approach using two variables to track the smallest and second smallest values seen so far. It falls under the "array traversal with state tracking" pattern.

- Plan:
  1. Initialize two variables, `first` and `second`, to infinity.
  2. Iterate through each number in the array:
     - If the number is less than or equal to `first`, update `first`.
     - Else if the number is less than or equal to `second`, update `second`.
     - Else (number is greater than both), we found a valid triplet → return True.
  3. If the loop ends without finding such a triplet, return False.

- Implement:
  See code below.

- Review:
  The algorithm correctly handles edge cases like arrays with <3 elements, duplicates, and non-consecutive valid triplets. It avoids brute-force O(n³) by maintaining only necessary state.

- Evaluate:
  The solution is optimal: it uses constant space and only one pass through the array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    print(solution.increasingTriplet([1, 2, 3, 4, 5]))     # True
    print(solution.increasingTriplet([5, 4, 3, 2, 1]))     # False
    print(solution.increasingTriplet([2, 1, 5, 0, 4, 6]))  # True (1 < 4 < 6 or 0 < 4 < 6)
    print(solution.increasingTriplet([1, 1, 1, 1]))        # False
