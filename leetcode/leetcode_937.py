class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []  # letter와 digit 을 구분해서 분류
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        # 2개 키를 포함한 람다식으로 정렬하기
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))  # 알파벳 순으로 정렬 , 동일 단어들만 있는경우 식별자로 정렬하기

        return letter + digit