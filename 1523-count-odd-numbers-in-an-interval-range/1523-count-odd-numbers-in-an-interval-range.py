class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 == 1 or high%2 == 1:
            return (high-low)//2+1
        else:
            return (high - low)//2
        