class Solution:

    def encode(self, strs: List[str]) -> str:
        em = ""
        for s in strs:
            em += '#' + str(len(s)) + '/' + s
        return em
    def decode(self, s: str) -> List[str]:
        i = 0
        fin = []
        w = ""
        l = 0
        while i < len(s):
            if s[i] == '#':
                i += 1
                while(s[i] != '/'):
                    l = l*10 + int(s[i])
                    i += 1
                i += 1
                for n in range(l):
                    w += s[i]
                    i += 1
                l = 0
                fin.append(w)
                w = ""
        return fin