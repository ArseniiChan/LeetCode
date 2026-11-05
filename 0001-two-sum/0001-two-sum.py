class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        #pre: array nums, integer target

        #post twoSum returns index of target sum


        #Design idea

        #nums = [2,7,11,15], target = 9

        #i = 0 
        # j = 1

        # 2 for loops going through the array and seeing if it = to the target

        # return nums[i, j]

        for i in range(len(nums)):
            for j in range(i + 1, (len(nums))):
                if nums[i] + nums[j] == target:
                    return [i, j]




        