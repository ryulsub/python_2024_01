# 1.핸드폰 번호 가리기
# "01012345678" 전화번호 문자열 phone_number ,전화번호 뒷4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(phone_number):
    newNumber = ""
    for index, item in  enumerate(phone_number):
        if len(phone_number) - 4 > index:
            newNumber += "*"
        else:
            newNumber += item
    return newNumber
a = solution("01012345678")
print(a)



