class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        total = sum(beans)
        mini = float('inf')

        for i in range(n):
            keep = beans[i] * (n - i)
            remove = total - keep
            mini = min(mini, remove)
        return mini
