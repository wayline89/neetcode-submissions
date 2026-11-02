class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for mot in strs:
            motsort = "".join(sorted(mot))
            res[motsort] = res.get(motsort, [])

            res[motsort].append(mot)
        return list(res.values())
