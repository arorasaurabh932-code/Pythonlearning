#create a class
class customer:
    bank_name='HDFC bank'#class
    def __init__(self,name,age,initamt):
        self.name=name #instance variable
        self.age=age
        self.balance=initamt
#local variable
    def deposit(self,amount):
        self.balance += amount
        print(f'deposit of {amount}is successful.Updated balance is {self.balance}')
c1=customer('john',31,5000)
print(c1.name)
print(c1.age)
print(c1.balance)

c2=customer('johny',21,6000)
print(c2.name) #instance variable
print(c2.age)
print(c2.balance)
c1.deposit(300)
c2.deposit(100000)
