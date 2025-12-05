class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        for n, count in freq.items():
            if count == 1:
                return n    
            

        