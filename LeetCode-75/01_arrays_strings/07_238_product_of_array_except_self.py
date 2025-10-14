"""
Problem: Product of Array Except Self
Difficulty: Medium
Category: Array / Prefix-Suffix Products
LeetCode Link: https://leetcode.com/problems/product-of-array-except-self/

Approach (UMPIRE):
- Understand: Given array nums, return array where answer[i] equals product of all elements except nums[i].
  Cannot use division, must be O(n) time. Key insight: product except self = left products × right products.
  
- Match: Prefix/Suffix products pattern - decompose problem into products from left and products from right.
  Similar to problems requiring information about "everything except current element."
  
- Plan: 
  1. Create arrays for left_products and right_products
  2. First pass (L→R): Build left_products where each index stores product of all elements to its left
  3. Second pass (R→L): Build right_products where each index stores product of all elements to its right
  4. Combine: answer[i] = left_products[i] × right_products[i]
  
- Implement: Three loops - build left products forward, build right products backward, combine for answer.
  Use cumulative products to avoid recalculation.
  
- Review: Handles edge cases (zeros in array, single elements). Works by decomposing problem into 
  independent subproblems. Each element's answer depends only on elements before and after it.
  
- Evaluate: Time O(n) with 3 passes. Space can be optimized to O(1) by reusing answer array 
  for left products and calculating right products on the fly.

Time Complexity: O(n) - three separate O(n) loops
Space Complexity: O(n) - for the output array (O(1) extra space if we don't count output)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Arrays to store products
        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n
        
        # Build left products: left_products[i] = product of all elements before i
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        # Build right products: right_products[i] = product of all elements after i
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
        
        # Combine: answer[i] = left[i] × right[i]
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]
        
        return answer


# Optimized O(1) space version (not counting output array)
class SolutionOptimized:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # First pass: store left products directly in answer array
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # Second pass: multiply by right products on the fly
        right = 1  # Running product from the right
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: {nums1}")
    print(f"Output: {solution.productExceptSelf(nums1)}")
    print(f"Expected: [24, 12, 8, 6]\n")
    
    # Test case 2 (with zero)
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: {nums2}")
    print(f"Output: {solution.productExceptSelf(nums2)}")
    print(f"Expected: [0, 0, 9, 0, 0]\n")
    
    # Test case 3 (two elements)
    nums3 = [2, 3]
    print(f"Input: {nums3}")
    print(f"Output: {solution.productExceptSelf(nums3)}")
    print(f"Expected: [3, 2]")
