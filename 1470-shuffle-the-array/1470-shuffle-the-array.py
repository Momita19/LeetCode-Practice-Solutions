class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        List = []
        for i in range(0, n):
            List.append(nums[i])
            List.append(nums[i+n])
        return List
        