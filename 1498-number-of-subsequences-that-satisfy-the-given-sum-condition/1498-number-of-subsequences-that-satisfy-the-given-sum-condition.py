class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()   
        count =0
       
        i = 0
        n = len(nums)
        j = n-1
        modulo = 10**9+7
        while i<= j:
            if nums[i]+nums[j] > target:
                j -= 1
            elif nums[i]+nums[j] <= target:
                count += pow(2, j-i, modulo)
                i += 1
        return count % modulo
                
                
        