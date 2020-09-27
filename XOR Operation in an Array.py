class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        xorCount = 0
        for i in range(n):
            xorCount ^= start + 2*i
        return xorCount

if __name__ == "__main__":
    solution = Solution()
    assert solution.xorOperation(5, 0) == 8
