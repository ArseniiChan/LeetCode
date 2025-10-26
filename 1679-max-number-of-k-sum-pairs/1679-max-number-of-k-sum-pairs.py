class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        left = 0 
        right = len(sorted_nums) - 1
        count = 0 

        while left < right:
            current_sum = sorted_nums[left] + sorted_nums[right]

            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        return count


        
        