# 5177 출력형식이 잘못되었습니다

K = int(input().rstrip()) #테스트 케이스의 수

for i in range(1, K+1):
    s1 = input().strip()
    s2 = input().strip()

    s1 = s1.lower()
    s2 = s2.lower()

    s1 = " ".join(s1.split())
    s2 = " ".join(s2.split())

    s1 = s1.replace("{", "(") .replace("[", "(").replace("}", ")").replace("]", ")")

    s1 = s1.replace(";", ",")

    s2 = s2.replace("{", "(").replace("[", "(").replace("}", ")").replace("]", ")")

    s2 = s2.replace(";", ",")

    s1 = s1.replace(' )', ')').replace('( ', '(').replace(') ',')').replace(' (', '(')

    s2 = s2.replace(' )', ')').replace('( ', '(').replace(') ', ')').replace(' (', '(')

    s1 = s1.replace(" ,", ",").replace(', ', ',').replace(" :", ":").replace(": ", ":").replace(" .", ".").replace(". ", ".")
    s2 = s2.replace(" ,", ",").replace(', ', ',').replace(" :", ":").replace(": ", ":").replace(" .", ".").replace(". ", ".")

    if s1 == s2:
        print(f"Data Set {i}: equal\n")
    else:
        print(f"Data Set {i}: not equal\n")



