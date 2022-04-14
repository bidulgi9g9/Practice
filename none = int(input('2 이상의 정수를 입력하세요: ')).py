none = int(input('2 이상의 정수를 입력하세요: '))
ntwo = 0

for i in range(2,none):
    if none%i == 0:
        ntwo = 1

if ntwo == 0:
    print('소수입니다')
else:
    print('소수가 아닙니다')