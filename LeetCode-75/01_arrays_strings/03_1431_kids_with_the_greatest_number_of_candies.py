"""
Problem: Kids With the Greatest Number of Candies
Difficulty: Easy
Category: Array
LeetCode Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Approach (UMPIRE):
- Understand: Determine which kids can have the greatest number of candies if given all extra candies.
  Multiple kids can have the greatest number simultaneously.
- Match: Array iteration with global comparison pattern. Need to find maximum once, then compare each element.
- Plan: 
  1. Find the current maximum number of candies any kid has
  2. For each kid, check if their candies + extraCandies >= maximum
  3. Store boolean results and return the array
- Implement: Single pass through array with O(1) lookup of precomputed maximum
- Review: Handles edge cases (multiple kids with same max, all kids can be greatest)
- Evaluate: Efficient solution - could optimize slightly with list comprehension but current approach is clear

Time Complexity: O(n) - one pass to find max + one pass to check each kid
Space Complexity: O(n) - for the result array (O(1) auxiliary space otherwise)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for each_kid in candies:
            if each_kid + extraCandies >= maximum:
                result.append(True) 
            else:
                result.append(False)
        
        return result


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    
    # Test case 1
    candies1 = [2, 3, 5, 1, 3]
    extraCandies1 = 3
    print(f"Input: candies = {candies1}, extraCandies = {extraCandies1}")
    print(f"Output: {solution.kidsWithCandies(candies1, extraCandies1)}")
    print(f"Expected: [True, True, True, False, True]\n")
    
    # Test case 2
    candies2 = [4, 2, 1, 1, 2]
    extraCandies2 = 1
    print(f"Input: candies = {candies2}, extraCandies = {extraCandies2}")
    print(f"Output: {solution.kidsWithCandies(candies2, extraCandies2)}")
    print(f"Expected: [True, False, False, False, False]\n")
    
    # Test case 3
    candies3 = [12, 1, 12]
    extraCandies3 = 10
    print(f"Input: candies = {candies3}, extraCandies = {extraCandies3}")
    print(f"Output: {solution.kidsWithCandies(candies3, extraCandies3)}")
    print(f"Expected: [True, False, True]")