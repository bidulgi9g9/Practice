ID = input("아이디를 입력하세요: ")
cnt = 0
while True:
    if ID == "홍길동":
        if cnt >= 3:
            print("3회 오류로 프로그램을 종료합니다.")
            break
        password = input("비밀번호를 입력하세요: ")
        while True:
            if password == "ABC":
                print("홍길동님 환영합니다.")
                break #break 대신에 너희가 짤 프로그램 코딩하면 될듯(잉크젯)
            else:
                cnt += 1
                if cnt >= 3:
                    break
                else:
                    password = input("비밀번호가 틀렸습니다. 다시 입력하세요: ")
    else:
        cnt += 1
        if cnt >= 3:
            print("3회 오류로 프로그램을 종료합니다.")
            break
        else:
            ID = input("아이디가 틀렸습니다. 다시 입력하세요: ")