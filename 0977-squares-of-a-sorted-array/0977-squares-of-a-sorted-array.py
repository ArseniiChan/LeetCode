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
        new_nums = []
        for n in nums:
            new_nums.append(n ** 2)
        return sorted(new_nums)
        