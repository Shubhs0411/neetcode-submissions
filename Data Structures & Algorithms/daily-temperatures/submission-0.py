class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        arr = [0] * n
        stack = []

        for i,idx in enumerate(temperatures):
            while stack and stack[-1][0] < idx:
                sn, sidx = stack.pop()
                arr[sidx] = i - sidx
            stack.append((idx, i))

        return arr
        