# Encapulation is act like a backend, which hide function from user, it contains instense of private class
class Encap_method:
    def __init__(self, acc, bal):
        self.__account=acc # __ make object private
        self.__balance=bal

    def getacc(self):
        return self.__account
    def getbal(self):
        return self.__balance
    
    def deposit(self, money):
        if money>0:
            self.__balance+=money
            print(f"Deposited: {money}")
        else:
            print("No money available yet")
    
    def withdraw(self,money):
        if money>0 and money<=self.__balance:
            self.__balance-=money
            print(f"Withdrawn: {money}")
        else:
            print("Insufficient balance")

class Bank_Encap:
    if __name__=="__main__":
        myacc=Encap_method("Xyz123",500) # It act as frontend to take methods from backend
        print(f"Account: {myacc.getacc()}")
        print(f"Balance: {myacc.getbal()}")

        myacc.deposit(2000)
        print(f"Balance after deposit: {myacc.getbal()}")   

        myacc.withdraw(200.00)
        print(f"Balance after withdraw: {myacc.getbal()}")

