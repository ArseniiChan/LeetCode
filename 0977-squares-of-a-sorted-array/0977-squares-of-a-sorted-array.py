#pre: array nums
#post: sortedSquares returns the array nums sorted and squared

#Design Idea
#Base case: if nums is empty we return []

#2 pointers for this problem
#for each element n times it by n
# left = 0, right = 1
# compare right to left, if left is > than right, you move right to left and you move left to right 
# but then why cant we just do for n in nums n x n and then the sorted function?

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n 
        left = 0
        right = n - 1
        i = n - 1

        while left <= right:
            left_sq = nums[left] ** 2 
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result[i] = left_sq
                left += 1 
            else:
                result[i] = right_sq
                right -= 1
            i -= 1
        return result
        