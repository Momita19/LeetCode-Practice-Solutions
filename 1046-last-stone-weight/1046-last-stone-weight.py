class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #loop till one element remains in the list
        while len(stones)>1:
#             sort in descending order
            stones.sort(reverse=True)
            x = stones[1]
            y = stones[0]
            
            if x == y:
                stones = stones[2:]
                print(stones)
            else:
                stones = stones[2:]
                print(stones)
                stones.append(y-x)
                print(stones)
        return stones[0] if stones else 0
        
        