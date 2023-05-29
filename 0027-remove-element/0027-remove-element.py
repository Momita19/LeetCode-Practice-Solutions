class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j = len(nums)-1
        
        while i<=j:
            if val == nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                j = j-1
            else: 
                i += 1
                print(i)
        return i
                
        