# CHALLENGE 1:

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self,x,y,z):
        sum = x*x + y*y + z*z
        return sum

point = Point(1,2,3)    
print("Sum of square of numbers: ",point.sqSum(1,2,3))


#************#
# CHALLENGE 2:


class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        while self.num1 != 0:
            return self.num1 / self.num2

obj = Calculator(94, 10)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())


#*******************#
# CHALLENGE 3


class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = 0

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

student = Student()

student.setName("Shruti Sharma")
student.setRollNumber(55)

print("Name:", student.getName())  
print("Roll Number:", student.getRollNumber())  


#*****************#
# CHALLENGE 4

class Account:

    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):

    def __init__(self,interestRate,title=None,balance=0):
        self.interestRate = interestRate
        Account.__init__(self,title,balance)

acc  = Account("Ashish", 5000)
savacc = SavingsAccount("Ashish", 5000, 5)
print("\nAccount Details: ")
print("Account Title:", acc.title)
print("Account Balance:", acc.balance)
print("\nSavings Account Details: ")
print("Savings Account Title:", savacc.title)
print("Savings Account Balance:", savacc.balance)
print("Savings Account Interest Rate:", savacc.interestRate)


#*******************#
# CHALLENGE 5

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
         return self.balance 
        
    def deposit(self,amount):
         if amount > 0:
            self.balance += amount
         
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount   

class SavingsAccount(Account):

    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
            
    def interestAmount(self):
        return (self.balance * self.interestRate)/100
    
demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print("Title: ",demo1.title)  
print("Balance after deposit:",demo1.getBalance())  
demo1.withdrawal(500)  
print("Balance after withdrawal: ",demo1.getBalance())  
print("Interest Rate: ",demo1.interestRate)  
print("Interest Amount: ",demo1.interestAmount())




