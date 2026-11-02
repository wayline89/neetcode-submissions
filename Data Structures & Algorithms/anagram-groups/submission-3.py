class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}

        for mot in strs:
            msort="".join(sorted(mot))
            res[msort]=res.get(msort,[])
            res[msort].append(mot)
        return list(res.values())