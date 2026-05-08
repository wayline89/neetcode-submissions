class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let gauche = 0;
        let maxProfit = 0;

        for (let droite = 1; droite < prices.length; droite++) {

            if (prices[droite] < prices[gauche]) {
                gauche = droite;
            } else {
                let profit = prices[droite] - prices[gauche];
                maxProfit = Math.max(maxProfit, profit);
            }
        }
        return maxProfit;
    }
}
