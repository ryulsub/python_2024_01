# review
words = ["apple","banana","cherry","date"]

def solution(arr):
    # {5: 2, 6: 1, 4: 1}
    result = {}
    for i in arr:
        length = len(i)
        if length in result:
            result[length] +=1
        else:
            result[length] = 1
        return result

a = solution(words)
print(a)





