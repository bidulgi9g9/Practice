from ctypes import sizeof


numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for letter in numbers:
    if letter % 2 == 0:
        print(str(letter) + "는 짝수입니다.")   
    else:
        print(str(letter) + "는 홀수입니다.")

