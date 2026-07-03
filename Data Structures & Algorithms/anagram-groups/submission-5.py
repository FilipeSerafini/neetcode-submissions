class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ["act","pots","tops","cat","stop","hat"]
        hm = {} # sorted str: [anagrams]
        for s in strs:
            srtd = str(sorted(s)) # list of chars
            if srtd in hm:
                hm[srtd].append(s)
            else:
                hm[srtd] = [s]
        # {act: [act, cat], opts: [pots, tops, stop], aht: [hat]}

        res = []
        for value in hm.values():
            res.append(value)
        # res = [[act, cat], [pots, tops, stop], [hat]]

        return res

        