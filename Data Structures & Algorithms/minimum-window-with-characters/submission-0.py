class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        ref, it = defaultdict(int), defaultdict(int)
        for c in t:
            ref[c] += 1
        
        res = [-1, -1]
        resLen = float("inf")
        have, need = 0, len(ref)
        l = 0
        for r in range(len(s)):
            c = s[r]
            it[c] += 1

            if c in ref and it[c] == ref[c]:
                have += 1

            while have == need:
                if (r-l+1 < resLen):
                    res = [l, r]
                    resLen = r - l + 1
                it[s[l]] -= 1
                if s[l] in ref and it[s[l]] < ref[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen == float("inf"):
            return ""
        return s[l:r+1]
