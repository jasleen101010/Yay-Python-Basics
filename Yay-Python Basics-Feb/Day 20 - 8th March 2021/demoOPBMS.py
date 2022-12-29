###############################################################################
#                   Project 3 - Bank Management System                        #
###############################################################################
# * --------------------------------------------------------------------------*
# * AUTHOR: Rahul Bordoloi <rahul.bordoloi@highradius.com>                    *
# * Github: https://github.com/rahulbordoloi                                  *
# * --------------------------------------------------------------------------*
# * DATE CREATED: 8 March, 2021                                               *
# * ************************************************************************"""


# Class Bank Account [Parent Class]
class BankAccount:

    """
    Parent Class Bank Account will contain basic information that will be common to all types of Bank Accounts.
    """

    # Class Variables
    numberOfAccounts = 0
    __accountNumbers = []

    # Default Constructor
    def __init__(self, accNumber = None, name = None, balance = 0):
        
        # Updating Instance Variables
        self.__accountNumber = accNumber
        self._name = name
        self.__balance = balance


        # Checking Rare/Invalid Cases
        if((accNumber) & (accNumber != -1)):
            self.__accountNumber = accNumber
        else:
            if self.__accountNumber in BankAccount.__accountNumbers:
                self.__accountNumber = BankAccount.__accountNumbers[-1] + 1
            else:
                self.__accountNumber = BankAccount.numberOfAccounts + 1

        # Updating Class Variables
        BankAccount.__accountNumbers.append(self.__accountNumber)
        BankAccount.numberOfAccounts += 1

    # Getters

    ## Method to Get Account Number of a Customer
    def get_AccNo(self):
        return self.__accountNumber

    ## Method to Get Name of a Customer
    def get_Name(self):
        return self._name

    ## Method to Get Balance of a Customer
    def _get_Balance(self):
        return self.__balance

    # Setters

    ## Method to Set Account Number of a Customer
    def set_account_number(self, value):
        self.__accountNumber = value

    ## Method to Set Name of a Customer
    def set_name(self, value):
        self._name = value

    ## Method to Set Balance of a Customer
    def _set_Balance(self, value):
        self.__balance = value


# Class Saving Account [Derived|Child Class]
class SavingAccount(BankAccount):

    """
    Derived Class to implement Saving Accounts.
    """

    # Default Constructor
    def __init__(self, accountNumber, name, balance, branchName):

        # Calling Parent Class Constructor
        super().__init__(accountNumber, name, balance)

        # Updating Instance Variables
        if branchName == '-1':
            self.branchName = "NCR"
        else:
            self.branchName = branchName

    # Withdraw Money
    def withdrawMoney(self, amount):

        bal = super()._get_Balance()
        if bal >= amount:
            bal -= amount
            super()._set_Balance(bal)
            print('Money Withdrawn Successfully!')
        else:
            print('Insufficient Funds to withdraw Money!')

    # Check Balance
    def checkBalance(self):
        print(f'Your Current Balance is : $ {super()._get_Balance()}')

    # Deposit Money
    def depositMoney(self, amount):

        bal = super()._get_Balance()
        bal += amount
        super()._set_Balance(bal)
        print('Money Successfully Deposited!')


# Class Fixed Deposit [Derived|Child Class]
class FixedDeposit(BankAccount):

    """
    Derived Class to implement Fixed Deposit Accounts.
    """

    # Default Constructor
    def __init__(self, accNumber, name, duration, amount, rateOfInterest):

        # Calling Parent Class Constructor
        super().__init__(accNumber, name)

        # Updating Instance Variables
        self.__duration = duration
        self.__amount = amount
        self.__rateOfInterest = rateOfInterest

    # Getters

    ## Method to Get the Duration of a Fixed Deposit Account
    def get_Duration(self):
        return self.__duration
    
    ## Method to Get the Amount Associated with a Fixed Deposit Account
    def get_Amount(self):
        return self.__amount

    ## Method to Get the ROI Associated with a Fixed Deposit Account
    def get_Rate_Of_Interest(self):
        return self.__rateOfInterest


    # Setters

    ## Method to Set the Duration of a Fixed Deposit Account
    def set_Duration(self, value):
        self.__duration = value
    
    ## Method to Set the Amount Associated with a Fixed Deposit Account
    def set_Amount(self, value):
        self.__amount = value

    ## Method to Set the ROI Associated with a Fixed Deposit Account
    def set_Rate_Of_Interest(self, value):
        self.__rateOfInterest = value


# Class Recurrring Deposit [Derived|Child Class]
class RecurringDeposit(BankAccount):

    """
    Derived Class to implement Recurring Deposit Accounts.
    """

    # Default Constructor
    def __init__(self, accNumber, name, duration, monthlyPayement, rateOfInterest):

        # Calling Parent Class Constructor
        super().__init__(accNumber, name)

        # Updating Instance Variables
        self.__duration = duration
        self.__monthlyPayment = monthlyPayement
        self.rateOfInterest = rateOfInterest

    # Getters

    ## Method to Get the Duration Associated with a Recurring Account
    def get_Duration(self):
        return self.__duration

    ## Method to Get the Monthly Payment Associated with a Recurring Account
    def get_Monthly_Payment(self):
        return self.__monthlyPayment

    ## Method to Get the Rate of Interet Associated with a Recurring Account
    def get_Rate_Of_Interest(self):
        return self.rateOfInterest   

    # Setters

    ## Method to Set the Duration Associated with a Recurring Account
    def set_Duration(self, value):
        self.__duration = value

    ## Method to Set the Monthly Payment Associated with a Recurring Account
    def set_Monthly_Payment(self, value):
        self.__monthlyPayment = value
    ## Method to Set the Rate of Interet Associated with a Recurring Account
    def set_Rate_Of_Interest(self, value):
        self.rateOfInterest = value 


# Main Method
def main():

    while True:

        print()
        print("*" * 30)
        print(" Welcome to XYZ Bank Pvt. Ltd. ")
        print("*" * 30, "\n")
        print("1. Create or Manage a Savings Account")
        print("2. Create or Manage a Fixed Deposit Account")
        print("3. Create or Manage a Recurring Deposit Account")
        print("4. Exit")

        choice = int(input("\nEnter your Choice : "))

        # Choice for Savings Account
        if choice == 1:
            
            print()
            print("*" * 5, "Welcome to the Savings Section", "*" * 5)
            n = int(input("What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

            # For New Users
            if n == 1:

                name = input("Enter your Name : ")
                accNo = int(input("Enter an Account Number of your Choice or Leave it Random [-1] : "))
                balance = int(input("Enter your Opening Balance : "))
                branch = input("Enter a Branch Name of your Choice or Leave it Random [-1] : ")
                savingsObj = SavingAccount(accNo, name, balance, branch) 
                print(f"\nSaving Account Created Successfully for {name}!\n")

            # For Existing Users
            if n == 2:
                
                x = int(input("Select : \n1. Know your Balance \n2. Withdraw Money \n3. Deposit Money\nEnter your Choice : "))

                # Checking Balance
                if x == 1:
                    savingsObj.checkBalance()

                # Withdrawing Money
                elif x == 2:
                    amount = int(input("Enter the Amount you want to Withdraw : "))
                    savingsObj.withdrawMoney(amount)

                # Depositing Money
                elif x == 3:
                    amount = int(input("Enter the Amount you want to Deposit : "))
                    savingsObj.depositMoney(amount)

                # Other Cases
                else:
                    print("Illegal Input, Please Try Again") 

        # Add up Functionalities Like : Change Name, Change Account Number etc etc.

        # Choice for Fixed Deposit Account 
        elif choice == 2:

            print()
            print("*" * 5, "Welcome to the Fixed Deposit Section", "*" * 5)
            n = int(input("What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

            # You Can Implement Stuffs Like Creating a New Fixed Deposit Account and Checking Attributes such as ROI, Amount etc.
            # Maturity Amount

            pass

        # Choice for Recurring Deposit Account
        elif choice == 3:

            print()
            print("*" * 5, "Welcome to the Recurring Deposit Section", "*" * 5)
            n = int(input("What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

            # You Can Implement Stuffs Like Creating a New Recurring Deposit Account and Checking Attributes such as ROI, Amount etc.
            # Maturity Amount
            pass

        # Choice for Exit
        elif choice == 4:
            exit(0)

        # Choice if no other Options Matches
        else:
            print("Sorry, Wrong Choice! Please Try Again!")

    # Create Accounts for Multiple Users and Handle them Accordingly.
    # To Inculcate try..catch..finally to Handle all Such Errors.
    # You can use File Handling Techniques to Import Data.


# Driver Code
if __name__ == '__main__':
    main()

###############################################################################
#                                 END                                         #
###############################################################################