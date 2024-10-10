N = int(input())

# 소수 판별 함수
def isPrime(num):
    if num <= 1:  # 1과 0은 소수가 아님
        return False
    if num == 2:  # 2는 소수
        return True
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

# 주어진 숫자가 소수인지 먼저 검사
if not isPrime(N):
    print("no")
else:
    # 숫자를 뒤집기 위한 리스트
    lstNum = list(str(N))[::-1]
    
    # 3, 4, 7이 있는지 확인
    for i in range(len(lstNum)):
        if lstNum[i] in ["3", "4", "7"]:
            print("no")
            break
        elif lstNum[i] == "6":
            lstNum[i] = "9"
        elif lstNum[i] == "9":
            lstNum[i] = "6"
    else:
        # 뒤집힌 숫자 생성 및 소수 여부 확인
        reversed_num = int("".join(lstNum))
        if isPrime(reversed_num):
            print("yes")
        else:
            print("no")
