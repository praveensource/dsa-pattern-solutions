"""
Problem: Best Time to Buy and Sell Stock
----------------------------------------
You are given an array `prices` where prices[i] is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy and a different day in the future to sell.

Return the maximum profit you can achieve. If no profit is possible, return 0.

Example:
---------
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Constraints:
------------
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

from typing import List

# ----------------------------------------------------------
# 🔹 Approach 1: Two-Pointer / Sliding Window Method
# ----------------------------------------------------------
# - Maintain two pointers:
#   i -> Buy day
#   j -> Sell day
# - If we find a smaller price at day j, move i forward.
# - Keep track of maximum profit during traversal.
#
# ⏳ Time Complexity: O(n)
# 💾 Space Complexity: O(1)
class SolutionPointer:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        i = 0  # pointer for buying
        for j in range(1, len(prices)):  # pointer for selling
            # Move i forward if a smaller buying price is found
            while prices[i] > prices[j]:
                i += 1
            # Calculate profit
            maxi = max(maxi, prices[j] - prices[i])
        return maxi


# ----------------------------------------------------------
# 🔹 Approach 2: Min-Price Tracking (Standard Method)
# ----------------------------------------------------------
# - Keep track of the minimum price seen so far.
# - At each step, compute the profit if sold today.
# - Update the maximum profit accordingly.
#
# ⏳ Time Complexity: O(n)
# 💾 Space Complexity: O(1)
class SolutionMinPrice:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # track minimum buying price
        max_profit = 0
        for price in prices:
            # update minimum price if lower found
            min_price = min(min_price, price)
            # calculate profit if sold today
            max_profit = max(max_profit, price - min_price)
        return max_profit


# ----------------------------------------------------------
# ✅ Example Run
# ----------------------------------------------------------
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    sol1 = SolutionPointer()
    print("Max Profit (Pointer Method):", sol1.maxProfit(prices))  # Output: 5

    sol2 = SolutionMinPrice()
    print("Max Profit (Min-Price Method):", sol2.maxProfit(prices))  # Output: 5
