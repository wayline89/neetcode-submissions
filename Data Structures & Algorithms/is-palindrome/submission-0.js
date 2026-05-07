class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const test = s.toLowerCase().replace(/[^a-z0-9]/g, "");
        let i = 0;
        let j = test.length-1;
        while (i < j) {
            if (test[i] !== test[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true
    }
}
