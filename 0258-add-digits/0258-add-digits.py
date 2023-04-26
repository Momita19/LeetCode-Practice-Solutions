class Solution:
    def addDigits(self, num: int) -> int:
        d=0
        while num > 0:
            d += num%10
            # print(d)
            num = num//10
            
            # print(num)
            if d > 9 and num == 0:
                num = d
                # print(num)
                d=0
            
                
        return d
