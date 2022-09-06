class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        last_idx = n - 1
        for i in range(n // 2):
            s[i], s[last_idx - i] = s[last_idx - i], s[i]

        return s
