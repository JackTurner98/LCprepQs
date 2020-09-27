class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        n = len(arr)

        for i, x in enumerate(arr):
            result += (((i + 1) * (n - i) + 1) // 2) * x
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOddLengthSubarrays([1, 2]))
