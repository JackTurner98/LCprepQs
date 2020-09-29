class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums
        missingNums = []
        numCount = {}
        for i in range(len(nums) + 1)[1:]:
            numCount[i] = 0

        for i in nums:
            numCount[i] += 1

        for i in numCount:
            if numCount[i] == 0:
                missingNums.append(i)
        return missingNums