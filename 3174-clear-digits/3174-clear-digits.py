class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        result = ""
        for ch in s:
            if ch.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        for ch in stack:
            result += ch
        return result



        



        