class Solution:
    def isPalindrome(self, s: str) -> bool:
        #pre: string s

        #post:  isPalindrome returns True if palindrome else false
    
        #design idea:
        # 2 pointers left = 0, right = len(s) - 1

        # then we are are going to have a while loop and inside of it have 2 while loops and if statement 

        left = 0 
        right = len(s) - 1
        while left < right:
            #check left side 
            while left < right and not s[left].lower().isalnum():
                left += 1

            #check right side
            while left < right and not s[right].lower().isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1 

        return True






