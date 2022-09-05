class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 예외 처리
        if s == " ":
            return True

        s = s.lower()  # 소문자로 변환
        new_str = ""

        for i in s:
            if i.isalnum():
                new_str += i
        n = len(new_str)

        for i in range(n // 2):
            if new_str[i] != new_str[n - i - 1]:
                return False
        return True