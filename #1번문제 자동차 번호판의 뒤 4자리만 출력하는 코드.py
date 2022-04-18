#1번문제 자동차 번호판의 뒤 4자리만 출력하는 코드
from os import remove


license_plate = "123 가 9876"
print(license_plate[6:])

#2번문제 문자열에서 콤마를 제거하는 코드를 작성하라  숫자가 붙어잇어야함
a = "90, 123, 876, 998"
remove_a1 = a.split(', ')[0]
remove_a2 = a.split(', ')[1]
remove_a3 = a.split(', ')[2]
remove_a4 = a.split(', ')[3]
print(remove_a1+remove_a2+remove_a3+remove_a4)

#3번문제 banana뒤에 orange를 추가해서 출력하는 코드
fruit_list = ['apple', 'pineapple', 'banana', 'grapes', 'strawberry']
fruit_list.insert(3, 'orange')
print(fruit_list)

#4번문제 슬라이스를 사용하여 짝수만 출력하는 코드
a = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
print(a[0::2])

#5번문제 변수 h가 새로운값 ('1', '2', 'c')를 가지도록 하는 코드
h = ('a', 'b', 'c')
lh = list(h)
lh[0:2] = ['1', '2']
h = tuple(lh)
print(h)

#6번문제 key값만 list로 작성해서 출력하는 코드 작성
inventory = {"메로나": [300, 200], '비비빅': [400, 3], '죠스바': [250, 100]}
inventorylist = list(inventory.keys())
print(inventorylist)

#7번문제 숫자를 입력받아서 짝수인지 홀수인지 구분하여 출력하는 코드
a = int(input("숫자를 입력해주세요:"))
if a % 2 == 0:
    print(str(a)+'는 짝수입니다.')
else :
    print(str(a)+'는 홀수입니다.')

#8번문제 성적점수를 입력받아 점수에 해당하는 등급 출력하는 코드
jumsu = int(input('점수를 입력해주세요:'))

if 91 <= jumsu <= 100 :
    print('A등급(grade) 입니다.')
elif 81 <= jumsu <= 90 :
    print('B등급(grade) 입니다.')
elif 71 <= jumsu <= 80 :
    print('C등급(grade) 입니다.')
elif 61 <= jumsu <= 70 :
    print('D등급(grade) 입니다.')
elif 0 < jumsu <= 60 :
    print('F등급(grade) 입니다.')
else :
    print("잘못된 점수입니다. 등급을 출력할 수 없습니다.")

#9번문제 웹사이트의 이름만 추출하는 코드작성
url = "http://www.daum.net"
print(url.split(".")[1])

#10번문제 
from random import *
cnt = 0
cnt2 = 0

while cnt <= 20:
    temp = randrange(1,101)
    cnt += 1
    if 40 <= temp <= 60 :
        temp1 = f'{cnt}번째 숫자는 {temp}이며, 범위내에 있습니다.'
        print(temp1)
        cnt2 += 1
    else :
        temp2 = f'{cnt}번째 숫자는 {temp}이며, 범위밖에 있습니다.'
        print(temp2)
string = f'범위내의 숫자는 총: {cnt2}번 나왔습니다.'    
print(string)








