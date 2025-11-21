class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        last_onebit = False
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                last_onebit = False
            else:
                i += 1
                last_onebit = True

        return last_onebit

