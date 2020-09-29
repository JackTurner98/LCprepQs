class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroIndexes = []
        for i, o, in enumerate(nums):
            if o == 0:
                zeroIndexes.append(i-len(zeroIndexes))
        for i in zeroIndexes:
            nums.pop(i)
            nums.append(0)
        return nums