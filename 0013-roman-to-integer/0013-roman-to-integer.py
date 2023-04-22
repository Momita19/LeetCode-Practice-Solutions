class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        value =0
        for i in range (0, len(s)-1):
            if (roman[s[i]] < roman[s[i+1]]):
                value -= roman[s[i]]
            else:
                value += roman[s[i]]
        value += roman[s[-1]]
        return value
            
            
        