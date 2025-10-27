class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        
        max_sum = current_sum
        
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)  # ← inside the loop!
        
        return max_sum / k  # ← properly indented