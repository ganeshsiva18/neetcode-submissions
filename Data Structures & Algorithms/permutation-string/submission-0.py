class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        ref_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        for c in s1:
            ref_dict[c] += 1 # Setup the reference

        for r in range(len(s2)):
            s2_dict[s2[r]] += 1
            if r - l + 1 > len(s1):
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1
            if s2_dict == ref_dict:
                return True

        return False