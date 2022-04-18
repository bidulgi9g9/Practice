# 60171922 이지우

print("가계부 프로그램을 실행합니다.")
print("="*30)
login = {"홍길동":"ABC"}
list_menu = {}

num = 0
count = 1
while(num < 3):
    name = input("아이디를 입력하세요: ")
    if(name == "홍길동"):
        passward = input("비밀번호를 입력하세요: ")
        if(passward == login.get("홍길동")):
            print("홍길동님 환영합니다")
            while(1): 
                item = int(input("메뉴를 선택하세요 1=출력 2=입력 3=삭제 0=종료: "))
                if(item == 1):                    
                    menu_name = []
                    menu_name_real = ""
                    k = 0
                    sum = 0          
                    if(list_menu != ""):     
                        for i in list_menu:
                            menu_name += i + " " + list_menu.get(i) + "원, "
                            k += 1
                            sum += int(list_menu.get(i))
                        menu_name += "총액은" + str(sum) + " 원입니다"
                        for j in menu_name:
                            menu_name_real += j
                        print(menu_name_real)
                    else:
                        print("출력할 내용이 없습니다")
                elif(item == 2):
                    menu = input("새로운 항목과 가격을 입력하세요: ")
                    list_save = menu.split() # 공백을 기준으로 스플릿
                    list_menu[list_save[0]] = list_save[1]
                    
                elif(item == 3):                    
                    menu_remove = input("삭제할 항목을 입력하세요: ")                    
                    print(menu_remove,list_menu.pop(menu_remove),"항목이 삭제되었습니다.")                    
                    list_menu = dict(list_menu)
                elif(item == 0):
                    exit = 1               
                    break
        else:
            passward = input("비밀번호가 틀렸습니다. 다시 입력하세요 :")
            count += 1
            if(count == 3):
                print("3회 오류로 프로그램을 종료합니다")
                break
    else:
        name = input("아이디가 틀렸습니다. 다시 입력하세요:")
        count += 1
        if(count == 3):
            print("3회 오류로 프로그램을 종료합니다")
            break
    if(exit == 1):
        print("가계부 프로그램을 종료합니다")
        break