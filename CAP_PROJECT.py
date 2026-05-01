
from datetime import datetime

class ATM:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.balance = balance
    self.pin = pin
    self.transactions = []
    self._add_transaction("ACCOUNT_OPENED ", 0.0)

  def _add_transaction(self, txn_type, amount):
    self.transactions.append({
      "date_time": datetime.now().strftime("%H:%M:%S"),
      "type": txn_type,
      "amount": amount,
      "balance": self.balance
    })

  def deposit(self):
    amt = float(input("Amount to be Added:"))
    self.balance += amt
    self._add_transaction("DEPOSIT", amt)
    print("New Balance is: ",self.balance)
  
  def withdraw(self):
    amt = float(input("Amount to be withdrawn:"))
    if amt > self.balance:
      print("Insufficient balance. Transaction cancelled.")
      return
    else:
      check = int(input("Enter you pin: "))
      if check == self.pin:
        print("PIN MATCHED SUCCESSFULLY")
        self.balance -= amt
        self._add_transaction("WITHDRAW", amt)
      else:
        print("WRONG PIN")
    print("Remaining Balance is: ",self.balance)
  
  def display_balance(self):
    self._add_transaction("BALANCE_CHECK ", 0.0)
    print("Current Bank Balance is: ",self.balance)

  def statement(self):
    print("\n--- MINI STATEMENT ---")
    print("Name:", self.first_name, self.last_name)
    print("Account ID:", self.account_id)
    print("Type\t\tAmount\t\tBalance\t\tDate Time")
    row_format = "{:<14}{:<16.2f}{:<16.2f}{}"
    for txn in self.transactions:
      print(row_format.format(txn["type"], txn["amount"], txn["balance"], txn["date_time"]))

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
account_id = int(input("Enter first 6 digit of account number: "))
account_type = input("Enter your account type: ")
pin = int(input("Enter your PIN: "))
balance = int(input("Enter Amount to deposit: "))
Acc_1 = ATM(first_name,last_name,account_id,account_type,pin,balance)

def atm():
    while True:
        print('\n ----ATM MENU----')
        print('1. Display Balance')
        print('2. Withdraw Amount')
        print('3. Deposit Money')
        print('4. Statement')
        print('5. Exit')

        choice = int(input("\n Enter your Choice: "))
        if choice == 1:
          Acc_1.display_balance()
        elif choice == 2:
          Acc_1.withdraw()
        elif choice == 3:
          Acc_1.deposit()
        elif choice == 4:
          Acc_1.statement()
        elif choice == 5:
            print("Thank You for using ATM")
            break
        else:
            print("Invalid Choice")

atm()