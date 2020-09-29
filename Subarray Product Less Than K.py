class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        memory = {}
        count = 0
        for i, num in enumerate(nums):
            window = 1
            tempArr = nums[i:i + window]
            while window <= len(nums) - i:
                sortarr = str(sorted(tempArr))
                if sortarr in memory or self.productofarray(tempArr) < k:

                    if sortarr not in memory:
                        memory[sortarr] = 0
                    memory[sortarr] += 1
                    count += 1
                    window += 1
                    tempArr = nums[i:i + window]
                else:
                    break
        return count

    def productofarray(self, arr):
        result = 1
        for i in arr:
            result *= i
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
