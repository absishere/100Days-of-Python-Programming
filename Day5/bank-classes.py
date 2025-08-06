class Account:
    def __init__(self, acc_no, bal):
        self.acc_no = acc_no
        self.bal = bal

    def debit(self, deb):
        self.bal -= deb
        print(f"Amount of Rs.{deb} was debited.")
        self.get_balance()

    def credit(self, cred):
        self.bal += cred
        print(f"Amount of Rs.{cred} was credited.")
        self.get_balance()

    def get_balance(self):
        print(f"Remaining balance is Rs.{self.bal}")

if __name__ == "__main__":
    acc_no = int(input("Enter your Account number: "))
    bal = int(input("Enter initial balance: "))
    acc = Account(acc_no, bal)

    deb = int(input("Enter your debit amount: "))
    acc.debit(deb)

    cred = int(input("Enter your credit amount: "))
    acc.credit(cred)