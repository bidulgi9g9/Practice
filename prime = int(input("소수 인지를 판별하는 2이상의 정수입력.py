prime = int(input("소수 인지를 판별하는 2이상의 정수입력 :"))
div = 2
while div <= prime :
    if prime % div != 0 :
        div = div + 1
    elif prime % div == 0 and div < prime :
        print("숫자", prime, "는 소수가 아닙니다.")
        break
    else :
        print("숫자", prime, "는 소수입니다.")
        break
    
        
        

