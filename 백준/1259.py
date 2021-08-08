while True:
    number = str(input())
    mid = len(number) // 2
    if number == '0':
        break

    elif len(number)% 2 == 0: # 짝수인 경우

        if number[:mid] == number[mid:]:
            print('yes')
        else:
            print('no')

    elif len(number)% 2 != 0:

        if number[:mid+1] == number[mid:]:
            print('yes')
        else:
            print('no')

while True:
    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')
