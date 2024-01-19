#1. 문자열 뒤집기
# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 함수를 완성해주세요.
# "bread"
def reverseStr(my_string):
    strList = list(my_string) # [b,r,e,a,d]
    strList.reverse() # [d,a,e,r,b]
    word = ""
    for i in strList:
        word += i
    return word
print(reverseStr("bread"))


#2. 미완성된 할 일 찾기
todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]

def haveto_List(todoList, finishedList):
    return [todoList[index] for index,item in enumerate(finishedList) if not item]

print(reverseStr("bread"))
print(haveto_List(todo_list,finished))

