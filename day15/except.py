try : # try는 에러가 날것 같은 구문을 적는곳
    num = int(input("숫자 입력:"))
    result = 10 /num
    print(f"결과는 {result}")
except Exception:
    print('에러났음')
else:
    print("에러없음~")
finally:
    print("상관없으니 보여주라")