class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:  # Current spot is empty
                # Check left neighbor
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                # Check right neighbor  
                right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                
                if left_empty and right_empty:
                    count += 1
                    flowerbed[i] = 1
        
        return count >= n