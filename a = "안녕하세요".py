idlist = []
pwlist = []

while True:
    menu1 = int(input("1번=로그인, 2번=회원가입, 3=주문, 4=주문취소, 5=관리자모드, 0=종료>>"))
    if menu1 == 1 :
        while True:
            Id1 = input("아이디를 입력해주세요:")
            if Id1 in idlist:
                Pw1 = input("패스워드를 입력해주세요:")
                Id11 = idlist.index(Id1)
                if pwlist[Id11] == Pw1 :
                    print("로그인에 성공하셨습니다.")
                    break
                else :
                    print("비밀번호 오류로 종료합니다.")
                    break
            elif len(idlist) == 0 :
                print("회원가입을 먼저 해주세요")
                break
            else :
                print("없는 아이디입니다.종료합니다.")
                break
    elif menu1 == 2 :
        Id2 = input("아이디를 입력해주세요:")
        Pw2 = input("비밀번호를 입력해주세요:")
        idlist.append(Id2)
        pwlist.append(Pw2)
    
        


            
                
            

