class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant, dire = deque(), deque()                                                                             
        for i, char in enumerate(senate):
            if char == "R":
                radiant.append(i)
                
            else:
                dire.append(i)
                
        #when they are not empty
        while dire and radiant:
            rIndex = radiant.popleft()
            
            dIndex = dire.popleft()
           
            if rIndex < dIndex:
                radiant.append(rIndex+n)
                
                
            else:
                dire.append(dIndex+n)
                
        return 'Radiant' if radiant else 'Dire'
        