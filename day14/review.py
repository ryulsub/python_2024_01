# class Dog:
#     def __init__(self, n):
#         self.name = n
#
#     def intro(self):
#         print(f"저는 {self.name} 입니다.")
#
# a = Dog('킹율')
# a.intro()
# b = Dog('흰둥이')
# b.intro()


class BankAccount:
    def __init__(self, account_number,owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balnace += amount
            return True
        else:
            print("금액을 잘못 입력 하였습니다.")
            return False

        def withdraw(self, amount):
            if 0 < amount and amount < self.balance:
                self.balance -= amount
                return True
            else:
                print("금액을 잘못 입력 하였습니다.")
                return False

            def get_balance(self):
                return self.balance

            def get_account(self):
                return f"Account: {self.account_number}, wner: {self.owner_name} balance: {self.balance}"

def bankSystem():

    globalAccount = {}

    while True:
        print("은행 계좌 시스템")
        print("1: 계좌 개설")
        print("2: 입금")
        print("3: 출금")
        print("4: 잔액 조회")
        print("5: 종료")
        systemNumber = input("선택: ")

        if systemNumber == "1":
            account_number = input("계좌 번호:")
            owner_name = input("소유자 이름:")
            globalAccount[account_number] = BankAccount(account_number,owner_name)
            print('계좌 개설이 완료 되었습니다!')

        elif systemNumber == "2":
            account_number = input("계좌 번호:")
            amount = int(input("입금액:"))
            if account_number in globalAccount and globalAccount[account_number].deposit(amount):
                print("입금 완료")
            else:
                print("입금 실패")

        elif systemNumber == "3":
            account_number = input("계좌 번호:")
            amount = int(input("출금액:"))
            if account_number in globalAccount and globalAccount[account_number].deposit(amount):
                print("출금 완료")


        elif systemNumber == "4":
            account_number = input("계좌 번호:")
            if account_number in globalAccount:
                print(globalAccount[account_number].get_account())
            else:
                print("계좌를 찾을 수 없습니다.")
            elif systemNumber == "5":
                print("은행 계좌 프로그램 종료합니다!.")
                break;



bankSystem()




