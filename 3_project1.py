class Bank:

    def __init__(self):
        self.pin=""
        self.balance=0
        self.welcome()
       

    def welcome(self):
        pin=input("Welcome to Prath Bank Please create your pin ")
        if(pin.strip() != ""):
            print("""
Your Account is created Successfully""")
            self.pin=pin
            self.menu()
        else:
            print("Pin cannot be empty")
            self.welcome() 


    def menu(self):

        user_input = input("""     
 How would you like to proceed ?

 Enter 1 to Change currect pin
 Enter 2 to deposit
 Enter 3 to withdraw
 Enter 4 to check balance
 Enter 5 to exit """)
        if user_input == "1":
            self.welcome()
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_bal()
        else :
            print("Bye Visit Again")   

    def check_pin(self):
        cur_pin=input("Please Enter Your Pin: ")
        if(self.pin==cur_pin):
            return True
        else:
            print("Try again Incorrect Pin")
            return False


    
    def deposite(self):
        amount=int(input("Enter the amount to add in your account "))
        self.balance=self.balance+amount
        print(amount," is credited to your Account ") 
        self.menu()

    def withdraw(self):
        if self.check_pin():
            amount=int(input("Enter the amount  "))
            if(self.balance>=amount):
                self.balance=self.balance-amount
                print(amount," is debited from  your Account ") 
            else :
                print("Insufficient Funds")
        self.menu()

    def check_bal(self):
        if self.check_pin():
            print("Your balance ",self.balance) 
        self.menu()
a=Bank()
