class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        const map = new Map();

        for (let i = 0; i < nums.length; i++) {

            if(!map.has(nums[i])){
                map.set(nums[i],1)
            }

            map.set(nums[i], map.get(nums[i]) + 1);
        }
        return [...map].sort((a,b)=>b[1]-a[1])[0][0]
    }
}
