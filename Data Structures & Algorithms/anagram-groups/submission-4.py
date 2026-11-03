class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}

        for mot in strs:
            mot_s="".join(sorted(mot))
            seen[mot_s]=seen.get(mot_s,[])
            seen[mot_s].append(mot)
        return list(seen.values())