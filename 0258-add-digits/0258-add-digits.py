class Solution:
    def addDigits(self, num: int) -> int:
        if num%9 != 0 or num == 0:
            return num%9
        else:
            return 9
        
