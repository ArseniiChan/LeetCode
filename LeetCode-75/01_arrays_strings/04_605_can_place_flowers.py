"""
Problem: Can Place Flowers
Difficulty: Easy
Category: Array / Greedy
LeetCode Link: https://leetcode.com/problems/can-place-flowers/

Approach (UMPIRE):
- Understand: Given a flowerbed array (0s and 1s) and number n, determine if we can plant n flowers 
  without violating the no-adjacent-flowers rule. 0 = empty, 1 = planted.
  
- Match: Greedy algorithm pattern - make locally optimal choices (plant as early as possible)
  to achieve global optimum.
  
- Plan: 
  1. Iterate through each position in flowerbed
  2. For each empty spot (0), check if both neighbors are safe (empty or don't exist)
  3. If safe, plant flower (set to 1) and increment counter
  4. Return true if we can plant at least n flowers
  
- Implement: Use bounds checking for edge positions, greedy planting approach
  
- Review: Handles edge cases (first/last positions), prevents double-counting by modifying array
  
- Evaluate: Optimal greedy solution. Alternative approaches like simulation would be less efficient.

Time Complexity: O(n) - single pass through the flowerbed array
Space Complexity: O(1) - only using constant extra space (count variable)
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:  # Current spot is empty
                # Check left neighbor (safe if at boundary or neighbor is empty)
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                # Check right neighbor (safe if at boundary or neighbor is empty)  
                right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                
                if left_empty and right_empty:
                    count += 1
                    flowerbed[i] = 1  # Plant flower to prevent adjacent planting
        
        return count >= n


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    
    # Test case 1
    print(solution.canPlaceFlowers([1,0,0,0,1], 1))  # Expected: True
    
    # Test case 2  
    print(solution.canPlaceFlowers([1,0,0,0,1], 2))  # Expected: False
    
    # Edge case: single empty spot
    print(solution.canPlaceFlowers([0], 1))  # Expected: True