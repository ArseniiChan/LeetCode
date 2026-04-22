class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #design idea 
        #pre: integer array nums 
        #post: threeSum returns all the triplets 

        #the sum should equal to 0

        #where would i put left pointer and right?

        #left = 0

        #right = idk 1 or len(nums) - 1
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result         