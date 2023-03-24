class BankApp:
    bname="ICICI"
    def __init__(self,cid,cname,bal=0):
        print("BankApp constructor")
        self.cid=cid
        self.cname=cname
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
    def withdraw(self,amt):
        if self.bal>=amt:
            self.bal=self.bal-amt
        else:
            print("U cannot withdraw ",amt," ur balance is:",self.bal," only")
    def balance_eqr(self):
        print("Ur balance is:",self.bal)
    def details(self):
        print("Bank name:",BankApp.bname)
        print("Cust name:",self.cname)
        print("cust id=",self.cid)
        print("cust balance:",self.bal)
b=BankApp(1001,"Shiva")
b.deposit(1000)
b.withdraw(2000)
b.details()
b.withdraw(500)
b.details()

b2=BankApp("1002","Shivakumar",10000)
print("**********")
b2.details()
b2.deposit(20000)
print("------------")
b2.details()
