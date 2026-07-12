class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_num = max(max_num, prices[j] - prices[i])
                
                    
        return max_num