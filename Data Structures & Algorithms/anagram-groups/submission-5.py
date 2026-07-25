class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_ = ''.join(sorted(s))
            res[sorted_].append(s)
        return list(res.values())