class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let count = 0;
        let max = 0;
        for (const num of nums) {
            if (num === 0) {
                max = Math.max(max, count);
                count = 0;
            } else if (num === 1) {
                count++;
                max = Math.max(max, count);
            }
        }

        return max;
    }
}
