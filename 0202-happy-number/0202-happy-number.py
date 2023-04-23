class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n not in seen):
            seen.add(n)
            print(seen)
            result = 0
            for i in str(n):
                result += int(i)**2
                
                print(i)
            if result == 1:
                return True
            
            
                
            n = result
            print(n)
            
                
           
        
        