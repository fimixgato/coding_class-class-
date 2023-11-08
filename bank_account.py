import random
class Bank_account():
    def bank_account_details():
        customer=input("Customer Name:")
        date=input("Date:")
        custumer_number=random.randint(1000,9999)
        print(f"Account number:{custumer_number}")
        start=(int(input(f"Hello {customer}, today's date is {date} how much would you like to start with:")))
        print("To withdraw input withdraw, to deposit input deposit and to check your balance input check balance")
        wwylt=input("What would you like to do?:")
        w="withdraw"
        d="deposit"
        c="check balance"
        
        if wwylt == w:
            amount=int(input("How much:"))
            start=start-amount
            print(f"Thank you.Your balance is now {start}")

        if wwylt == c:
            print(f"Your balance is {start}")
            
        if wwylt == d:
            amount=int(input("How much:"))
            start=start+amount
            print(f"Your balance is now {start}")
my_bankaccount=Bank_account
my_bankaccount.bank_account_details