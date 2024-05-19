'''
Encapsulation is the concept of hiding the implementation details of an object from the outside world and only exposing the necessary information through public methods.

Encapsulation helps protect the object's internal state from external interference and misuse.

In Python, you can achieve encapsulation using private attributes and methods, denoted by a double underscore prefix (__).

'''
class BankAccount:
    def __init__(self, account_number: int,balance: float) -> None:
        # Private attribute
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if self.__balance - amount < 0:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balaance(self) -> float:
        return self.__balance

bc = BankAccount(12345, 1000)
bc.deposit(500)
bc.withdraw(300)
print(bc.get_balaance())

# In this example, the __account_number and __balance attributes are private, meaning it can't be accessed directly from outside the class. 
# We interact with it through the deposit, withdraw, and get_balance methods.