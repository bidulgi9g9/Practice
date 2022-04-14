month = int(input('월 입력?'))
if 4<= month <=5 :
    print('봄')
elif month == 6 or month == 7 or month == 8 :
    print('여름')
elif month == 9 or month == 10 :
    print('가을')
elif 1 <= month <=3 or 11 <= month <= 12 :
    print("겨울")