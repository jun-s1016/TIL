#########################################
#1. 숫자가 양수인지 음수인지 판별하는 함수, 단 0은 0을 출력하기
def check_sign(num):
    if num > 0:
        return "양수"
    elif num < 0:
        return "음수"
    else :
        return "0"

print(check_sign(5)) # 양수 
print(check_sign(-10)) # 음수
print(check_sign(0)) # 0
#########################################