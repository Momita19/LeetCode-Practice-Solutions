class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = 0
        List =[]
        for i in range(0, len(nums)):
            res += nums[i]
            List.append(res)
            
        return List