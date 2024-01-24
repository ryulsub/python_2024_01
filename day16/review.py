# 2.영어가 싫어요
# 문자열 numbers가 매개변수로 주어질때, numbers 를 정수로 바꿔 return하도록 solution 함수를 완성해 주세요.

def solution(numbers):
    numList = {"zero","one","two", "three","five","four","five", "six","seven","eight","nine"}
    for index, item in enumerate(numList):
        numbers = numbers.replace(item,str(index))
    return int(numbers)

print(solution("onefourzerosixseven"))
