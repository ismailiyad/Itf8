import datetime


class BackAccount:

    def __init__(self,national_id,client_name):
        self.national_id = national_id
        self.client_name = client_name
        self.balance = 0
        self.transaction = []



    def withdraw (self,amount):

        if amount > self.balance or amount <= 0:
            print(f"Invalid Amount {amount} for withdrawal transaction")
        else:
            transaction = {
                "amount": amount,
                "date": str(datetime.datetime.now()),
                "type": "withdrawal"
            }
            self.transaction.append(transaction)
            self.balance -= amount
            print("withdrawal Done successfully")

    def deposit (self,amount):
        if amount <= 0:
            print(f"Invalid Amount {amount} for deposit transaction")
        else:
            self.balance += amount
            transaction = {
                "amount": amount,
                "date": str(datetime.datetime.now()),
                "type": "deposit"
            }
            self.transaction.append(transaction)

            print("Deposit Done successfully")

    def print_transaction_history(self):
        print("Amount\t|Type\t|Date")
        print("_____________________________")
        for i in self.transaction:
            print(f"{i.get('amount')}\t|{i.get('type')}\t|{i.get('date')}")
            print("_____________________________")
            print(f">>>> Total balance = {self.balance}")



ismail_account = BackAccount (400827309,"Ismail Ismail")

print(ismail_account.national_id)
print(ismail_account.client_name)
ismail_account.deposit(120)
ismail_account.print_transaction_history()
