class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find pairs with highest difference
        #where bigger number is after
        #starts from the back of the array to first item
        #if no positive result output 0

        change = 0
        for i in range(len(prices)-1,0,-1):
            for j in range(i-1,-1,-1): 
                if change < prices[i] - prices[j]:
                    change = prices[i] - prices[j]

        return change
            


        