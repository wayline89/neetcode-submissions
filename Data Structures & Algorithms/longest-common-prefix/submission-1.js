class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let longest = strs[0];

        for (const mot of strs) {
            while (!mot.startsWith(longest)) {
                longest = longest.slice(0, -1);
                if(longest === "")return "";
            }
        }return longest;
    }
}
