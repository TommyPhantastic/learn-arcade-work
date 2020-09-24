# class Transaction:
#     def __init__(self, my_date, my_amount, my_account):
#         self.date = ""
#         self.amount = 0
#         self.account = ""
#
# def main():
#     my_transaction = Transaction()
#     my_transaction.date = "9/23/2020"
#     my_transaction.amount = 10
#
# class Transaction:
#     def __init__(self, my_date, my_amount, my_account):
#         self.date = my_date
#         self.amount = my_amount
#         self.account = my_account
#
# def main():
#     my_transaction = Transaction("9/20/2020", 10, "320984230981")
#
# main()
#
# class Transaction:
#     transaction_count = 0

class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        if self.weight < 10:
            print("Yip! says", self.name)
        else:
            print("Woof! says", self.name)

def main():
    my_dog = Dog()
    my_dog.name = "Spot"
    my_dog2 = Dog()
    my_dog2.name = "Rover"


    my_dog.bark()


main()