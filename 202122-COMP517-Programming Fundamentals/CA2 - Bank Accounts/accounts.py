# import section
import random
import datetime

# class1: BasicAccount
class BasicAccount():
    """
        Basic account is an account consisted of:
            1. account name, string
            2. account number, int
            3. balance, float
            4. card number, string (if any)
            5. card expired date, tuple(int, int) (if any)
    """

    # class variables
    acNum = 0  # account number for each account
    all_cardNum = []  # store all card number to make sure the new one doesn't duplicate

    @classmethod
    def generate16(cls):
        """
            calculate the random 16 digits card number
            parameters:
                none
            return:
                string of 16 digits card number
        """
        all_num = [str(i) for i in range(10)]  # list of string of 0-9 digits
        while True:
            # create 16 digits string
            out = ''  # starting output string
            for i in range(16):  # 16 iterations
                out += random.choice(all_num)  # random string of a single digit and concatenate it to out
            # check duplicate
            if out not in cls.all_cardNum:
                cls.all_cardNum.append(out)
                break
        return out

    def __init__(self, acName, openingBalance):
        self.name = acName
        self.balance = float(openingBalance)
        BasicAccount.acNum += 1  # increase the account number by 1
        self.acNum = BasicAccount.acNum

    def __str__(self):
        """
            string to show type of account, account name, account number, and balance
        """
        return 'The balance of the BasicAccount of ' + self.name + '(acNum: ' + str(self.acNum) + ')' + ' is ' + str(
            self.balance)

    def deposit(self, amount):
        """
            deposit the amount
            parameters:
                deposit amount
            return:
                none
        """
        if amount < 0:  # if users deposit negative amount, do nothing
            pass
        else:  # if users deposit >= 0
            self.balance += amount  # add the balance by the given amount

    def withdraw(self, amount):
        """
            withdraw the amount
            parameters:
                withdraw amount
            return:
                none
        """
        # case 1: not enough money to withdraw
        if amount > self.balance:
            print('Can not withdraw £' + str(float(amount)))
        # case 2: can withdraw money
        else:
            new_balance = self.balance - amount  # the new balance
            print(self.name + ' has withdrawn £' + str(float(amount)) + '. New balance is £' + str(new_balance))
            self.balance = new_balance  # update balance

    def getAvailableBalance(self):
        """
            In this case, the available balance is equal to balance
        """
        return self.balance

    def getBalance(self):
        return self.balance

    def printBalance(self):
        print(self)  # print the string in the __str__

    def getName(self):
        return self.name  # get the account name

    def getAcNum(self):
        return str(self.acNum)  # get the account number (string)

    def issueNewCard(self):
        """
            create a new card number and its expire date
        """
        self.cardNum = self.generate16()  # create 16 digits card number
        time_now = datetime.datetime.now()  # get the current time
        string_year = str(time_now.year)  # string of the current year
        last_two_digit = int(string_year[len(string_year) - 2:])  # extract the last 2 digit of the year
        self.cardExp = (time_now.month, last_two_digit + 3)  # tuple of (month, year + 3)

    def closeAccount(self):
        """
            withdraw all balance and return True
        """
        self.withdraw(self.balance)
        return True

# class2: PremiumAccount
class PremiumAccount(BasicAccount):
    """
        Premium account is an upgraded account consisted of:
            1. account name, string
            2. account number, int
            3. balance, float
            4. card number, string (if any)
            5. card expired date, tuple(int, int) (if any)
            6. overdraft, boolean
            7. overdraft limit, float
    """

    def __init__(self, acName, openingBalance, initialOverdraft):
        super().__init__(acName, openingBalance)
        self.overdraftLimit = float(initialOverdraft)
        self.overdraft = False  # users hasn't used overdraft yet

    def __str__(self):
        """
            string to show type of account, account name, account number, balance, and the remaining overdraft
        """

        # calculate the remaining overdraft
        if self.balance >= 0:  # case 1: balance >= 0
            remaining = self.overdraftLimit
        else:  # case 2: balance < 0
            remaining = self.overdraftLimit + self.balance
        return 'The balance of the PremiumAccount of ' + self.name + '(acNum: ' + str(self.acNum) + ')' + \
               ' is ' + str(self.balance) + ' and the remaining overdraft is ' + str(remaining)

    def setOverdraftLimit(self, newLimit):
        self.overdraftLimit = float(newLimit)

    def getAvailableBalance(self):
        return self.balance + self.overdraftLimit

    def withdraw(self, amount):
        """
            withdraw the amount
            parameters:
                withdraw amount
            return:
                none
        """

        if amount > self.balance + self.overdraftLimit:  # case 1: not eligible to withdraw
            print('Can not withdraw £' + str(float(amount)))
        else:  # case 2: eligible to withdraw
            new_balance = self.balance - amount
            print(self.name + ' has withdrawn £' + str(float(amount)) + '. New balance is £' + str(new_balance))
            self.balance = new_balance  # update the balance
            # update overdraft boolean
            if self.balance < 0:
                self.overdraft = True
            else:
                self.overdraft = False

    def deposit(self, amount):
        """
            deposit the amount
            parameters:
                deposit amount
            return:
                none
        """

        if amount < 0:  # if users deposit negative amount, do nothing
            pass
        else:  # if users deposit >= 0
            self.balance += amount  # add the balance by the given amount
        # update overdraft boolean
        if self.balance < 0:
            self.overdraft = True
        else:
            self.overdraft = False

    def closeAccount(self):
        """
            check whether the user can close the account or not.
            if eligible to close the account, withdraw all balance.
            parameters:
                none
            return:
                boolean
        """

        if self.balance < 0:  # case 1: not eligible to close the account
            print('Can not close account due to customer being overdrawn by £' + str(self.balance))
            return False
        else:  # case 2: eligible to close the account
            self.withdraw(self.balance)
            return True
