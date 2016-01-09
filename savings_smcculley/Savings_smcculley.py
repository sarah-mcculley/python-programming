class Savings(object):
    def __init__(self, alias, interest, balance = 0.00):
        self.__alias = alias
        self.__interest = interest
        self.__balance = balance

    def __str__(self):
        return "The savings called " + self.__alias + " has ${:,.2f}".format(self.__balance)

    def __calcInterest(self):
        new_balance = (self.__interest * self.__balance) + self.__balance
        self.__balance = new_balance
        return self.__balance

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias):
        if alias == "":
            print("You must give your savings account an alias.")
        else:
            self.__alias = alias

    def deposit(self, deposit):
        self.__deposit = deposit
        self.__balance = self.__balance + deposit
        self.__calcInterest()

def main():
    Larz = Savings("college", 0.05)
    Larz.alias = "car"
    Larz.deposit(5000)
    print(Larz)

main()


