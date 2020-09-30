class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Brute Force
        # m = 0
        # for i, x in enumerate(prices):
        #     n = max(prices[i:]) - x
        #     if n > m:
        #         m = n
        # return m

        curMax = 0
        longMax = 0
        for i in range(1, len(prices)):
            print(i)
            curMax = max(curMax + prices[i] - prices[i - 1], 0)
            longMax = max(longMax, curMax)
        return longMax
