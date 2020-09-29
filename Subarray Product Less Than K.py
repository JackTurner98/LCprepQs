class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        result = 0
        product = 1
        left = 0
        right = 0
        while right < len(nums):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            result += right-left+1
            right += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
