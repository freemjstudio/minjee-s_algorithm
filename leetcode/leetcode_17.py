class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if len(digits) == 0:
            return answer
        number = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs',
                  8: 'tuv', 9: 'wxyz'}

        def dfs(index, total):
            if len(total) == len(digits):
                answer.append(total)
                return
            for i in range(index, len(digits)):  # 0, 1 digits = '23'
                for x in number[int(digits[i])]:
                    dfs(i + 1, total + x)

        dfs(0, "")

        return answer