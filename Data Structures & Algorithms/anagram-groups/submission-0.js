class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();
        for (const char of strs) {
            const mot = char.split("").sort().join("");
            if (!map.has(mot)) {
                map.set(mot, []);
            }
            map.get(mot).push(char);
        }
        return [...map.values()];
    }
}
