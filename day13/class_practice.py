# class_practice
class Dog:
    # 구조체는 직접 수정불가
    def __init__(self,n):
        self.hp = 100   # max 200
        self.stress = 50 # max 100
        self.name = n

     # 함수의 존재 이유는 구조체 데이터 보호

    def eating(self):
        if(self.hp >= 200):
            print('체력이 꽉 찼습니다.')
            print(f'현재 체력은 {self.hp}입니다.')
            self.hp = 200
        else:
            self.hp += 50

a = Dog('mega')
a.eating()
a.eating()
a.eating()
a.eating()