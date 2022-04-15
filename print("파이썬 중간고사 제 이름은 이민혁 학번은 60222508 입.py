print("파이썬 중간고사 제 이름은 이민혁 학번은 60222508 입니다.")
print("=" * 15)
inkjet = [100, 20]
laserjet = [200, 50]
price = 200000

while True:
    num = int(input("명령을 입력하세요 (1=사용 2=상태 3=보충 4=종료)>>"))
    if num == 1 :
        prt1 = int(input("프린터를 선택하세요 (1=잉크젯 2=레이저젯)>>"))
        if prt1 == 1 :
            page1 = int(input("몇 장 프린트 하시겠습니까?>>"))
            inkjet[0] -= page1 
            inkjet[1] -= int(page1/10)
        elif prt1 == 2 :
            page2 = int(input("몇 장 프린트 하시겠습니까?>>"))
            laserjet[0] -= page2 
            laserjet[1] -= int(page2/10)
        else :
            print('잘못된 명령입니다.')
    elif num == 2 :
        print("잉크젯 상태 종이 %d 토너 %d" %(inkjet[0], inkjet[1]))
        print("레이저젯 상태 종이 %d 토너 %d" %(laserjet[0], laserjet[1]))
        print("잔액", price)
    elif num == 3 :
        prt2 = int(input("보충하실 프린터를 선택하세요 (1=잉크젯 2=레이저젯)>>"))
        if prt2 == 1 :
            page3 = int(input("종이 수를 입력하세요>>"))
            toner1 = int(input("토너 수를 입력하세요>>"))
            inkjet[0] += page3
            inkjet[1] += toner1
            price = price - page3*100 - toner1*200

        elif prt2 == 2 :
            page4 = int(input("종이 수를 입력하세요>>"))
            toner2 = int(input("토너 수를 입력하세요>>"))
            laserjet[0] += page4
            laserjet[1] += toner2
            price = price - page4*100 - toner2*200

        else :
            print("잘못된 명렁입니다.")
    elif num == 4 :
        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못된 명령입니다.")

    
        