class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                t_t, t_i, = stack.pop()
                res[t_i] = i - t_i
            stack.append((v, i))
        return res
