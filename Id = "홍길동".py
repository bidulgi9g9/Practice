Id = "홍길동"
Pw = 1234
cnt = 0
cnt1 = 0
Id1 = input("아이디를 입력하세요:")

while True : 
    if Id1 == Id:
        while True:
            Pw1 = int(input("패스워드를 입력하세요:"))
            if Pw1 == Pw :
                print("로그인 성공!")
                break
            elif Pw1 != Pw and cnt < 3:
                print("패스워드를 잘못입력하셨습니다.(",3 - cnt,"번 남았습니다.)")
                cnt += 1
            else :
                break
    elif Id1 != Id and cnt < 3 :
        print("아이디를 잘못입력하셨습니다.다시입력해주세요(",3 - cnt,"번 남았습니다.)")
        cnt += 1
    else :
        print("3회오류로 프로그램을 종료합니다.")
        break
