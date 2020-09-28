class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        # Brute Force but optimized by checking mid requirements mid loop
        result = 0
        for i, x in enumerate(arr):
            for j, y in enumerate(arr):
                if j <= i:
                    continue
                if abs(x - y) <= a:
                    for k, z in enumerate(arr):
                        if k <= j:
                            continue
                        if abs(y - z) <= b:
                            if abs(x - z) <= c:
                                result += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    assert solution.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3) == 4