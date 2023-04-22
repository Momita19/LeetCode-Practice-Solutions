class Solution(object):
    def containsDuplicate(self, nums):
        list2 = list(set(nums))
        return len(list2) != len(nums)
        """
        :type nums: List[int]
        :rtype: bool
        """
        