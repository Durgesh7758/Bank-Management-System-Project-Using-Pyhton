##class user():
##    _count=0
##    def __init__(self,name,gender,salary):
##        self.name=name
##        self.gender=gender
##        self.salary=salary
##        user._count = user._count +1
##        self._account = user._count
##
##    def showdatabase(self):
##        print (f'Name-:{self.name}\nGender-: {self.gender}\nSalary-: {self.salary}')
##        print(f"Account Number-: {self._count}")
##
##class Bank(user):
##    __balance = 0
##
##    def __init__ (self,name,gender,salary):
##        self.name = name
##        self.gender = gender
##        self.salary = salary
##        Bank.__count = 222100000765
##        self.account = f'Bank_Ac_No-: {Bank.__count}'
##
##    def deposite(self,amount):
##        self.__balance = self.__balance + amount
##        print("Amount Deposited Successfully...!")
##        print(f"Your Current Balance Is-: {self.__balance}")
##
##    def withdraw (self,amount):
##
##        if amount > self.__balance:
##            print("Insufficient Balance...!")
##            print(f"Your Current Balance Is-: {self.__balance}")
##
##        elif amount >=100 and amount <= self.__balance:
##            self.__balance = self.__balance - amount
##            print("Amount Debited Successfully...!\nThank You For Visiting...!")
##            print(f"Your Current Balance Is-: {self.__balance}")
##
##        elif amount < 100:
##            print("You Cannot Withdraw Less Than 100")
##            print(f"Your Current Balance Is-: {self.__balance}")
##
##    def viewbalance(self):
##        print(f"Name-: {self.name}\nGender-: {self.gender}\nSalary-: {self.salary}\n Current Balance-: {self.__balance}")
##
##    def transfer(self,amt,user):
##       
##        if amt > self.__balance:
##            print("Insufficient Balance...!")
##            print(f"Your Current Balance Is-: {self.__balance}")
##
##        elif 1 <= amt  and amt <= self.__balance :
##            self.__balance=self.__balance - amt
##            print("Amount Transfer Successfully...!")
##            print(f"Your Current Balance Is-: {self.__balance}")
##
##        elif amt < 1:
##            print("You Cannot Transfer Amount Less Than 1")
##            print(f"Your Current Balance Is-: {self.__balance}")
##
##
##ob1=Bank("Darsh","Male",100000)
##ob2=Bank("Harsh","Male",120000)
##ob3=Bank("Aadarsh","Male",103000)
##ob4=Bank("Sangharsh","Male",100400)
##ob5=Bank("Darshan","Male",100005)




##class User():
##    __count = 0
##    def __init__(self,name,gender,salary):
##        self.name=name
##        self.gender=gender
##        self.salary=salary
##        User.__count = User.__count + 1
##        self.__account = User.__count
##
##    def showdetails(self):
##        print(f"Name : {self.name}\nGender : {self.gender}\nSalary : {self.salary}")
##        print("+------------------------------------------------+")
##        print("Account No : ", self.__account)
##
##class Bank():
##    __balance = 0
##    __bankname = "HDFC Bank".center(30)
##    __usercount = 0
##
##    def __init__(self,name,gender,mobile,salary,email,pin,aadhar):
##        self.name=name
##        self.gender=gender
##        self.mobile=mobile
##        self.salary=salary
##        self.email=email
##        self.__pin=pin
##        self.aadhar=aadhar
##        Bank.__usercount = Bank.__usercount + 1
##
##    def deposite(self,amount):
##        self.__balance=self.__balance + amount
##        print("Amount Deposited Successfully...!")
##        print("+------------------------------------------------+")
##        print("Your Current Balance Is -:", self.__balance)
##
##    def withdraw(self,amount):
##        if amount > self.__balance:
##            print("Insufficient Balance")
##            print("+------------------------------------------------+")
##            print("Your Current Balance Is -:", self.__balance)
##            
##        elif 100<= amount or amount<= self.__balance:
##            self.__balance = self.__balance - amount
##            print("Thank You For Visiting Our Branch...!")
##            
##        elif amount < 100:
##            print("You Can't Withdraw Amount Less Than 100")
##            print("Your Current Balance Is -:", self.__balance)
##
##    def viewbalance(self):
##        print(f"Name -: {self.name}\nGender -: {self.gender}\nCurrent Balance -: {self.__balance}")
##
##
##    def viewdetails(self):
##        print(f"Name -: {self.name}\nGender -: {self.gender}\nSalary -: {self.salary}\nCurrent Balance -: {self.__balance}\nMobile No. -: {mobile}")
##        print("Aadhar No -: ", self.aadhar)
##        print("Account No -: ",acn)
## 
##
##    def transfer(self,amt,user):
##        if amt > self.__balance:
##            print("Insufficient Balance")
##            print("+------------------------------------------------+")
##            print("Your Current Balance Is -:", self.__balance)
##
##        elif amt>= 1 and amt<=self.__balance:
####            user.deposite(amt)
##            self.__balance = self.__balance - amt
##            print("Amount Transfer Successfully")
##            print("+------------------------------------------------+")
##            print("Your Current Balance Is -:", self.__balance)
##
##        elif amt < 1:
##            print("You Can't Transfer Amount Less Than 1")
##            print("+------------------------------------------------+")
##            print("Your Current Balance Is -:", self.__balance)
##
##    def getusername(self):
##        return self.name
##
##    def getpin(self):
##        return self.__pin
##
##    def logindata(self):
##        return [self.name, self.__pin]
##
##    def __str__ (self):
##        return f"{self.name} {self.__pin}"
##
##users = {}
##
##while True:
##    print("+------------------ Wel-Come To Durgesh's Bank------------------------+")
##    
##    print("|+----------------------------------+|")
##    print("| Sr.No |          Steps             |")
##    print("|+----------------------------------+|")
##    print("| 1.    |       Create Account       |")
##    print("|+----------------------------------+|")
##    print("| 2.    |          Login             |")
##    print("|+----------------------------------+|")
##    print("| 3.    |           Exit             |")
##    print("|+----------------------------------+|")
##    
##    print("+------------------------------------------------+")
##    choice = input("Enter Your Choice -: ")
##    print("+------------------------------------------------+")
##    
##    print("")
##
##    if choice == "1":
##        while True:
##            name=input("Enter Your Name -: ")
##            print("------------------------------------------------")
##            if name.isalpha():
##                break
##            else:
##                print("Invalid Name...!\nPlease Enter Only Characters...!")
##                print("------------------------------------------------")
##                
##                
##        while True:
##            print("Select Your Gender")
##            print("1.Male")
##            print("2.Female")
##            print("3.Other")
##            print("------------------------------------------------")
##            gender=input("Enter Your Choice -: ")
##    
##            if gender == '1':
##                print("Male")
##                gender = "Male"
##                break
##            elif gender == '2':
##                print("Female")
##                gender = "Female"
##                break
##            elif gender == '3':
##                print("Other")
##                gender = "Other"
##                break
##            print("------------------------------------------------")
##
##            
##            if gender.isdigit():
##                break
##            else:
##                print("Invalid Choice...!\nPlease Enter Valid choice...!")
##                print("+------------------------------------------------+")
##
##        while True:
##            mobile = input("Enter Your Mobile Number -: ")
##            print("+------------------------------------------------+")
##            if mobile.isdigit() and len (mobile) == 10:
##                break
##            else:
##                print("Invalid Input...!\nPlease Enter Only Numbers that length should be 10...!")
##                print("+------------------------------------------------+")
##                
##             
##        while True:
##            salary = input("Enter Your Salary -: ")
##            print("------------------------------------------------")
##            if salary.isdigit():
##                salary=int(salary)
##                break
##            else:
##                print("Invalid Input...\nPlease Enter Only Numbers...!")
##                print("+------------------------------------------------+")
##
##        while True:
##            email = input("Enter Your Email-ID -: ")
##            print("+------------------------------------------------+")
##            break
##                
##        while True:
##            pin = input("Set Your Password (PIN) -: ")
##            print("+------------------------------------------------+")
##            if pin.isdigit() and len(pin) == 4:
##                pin = int(pin)
##                break
##            else:
##                print("Invalid Input...!\nPlease Enter Only Numbers that length should be 4...!")
##                print("+------------------------------------------------+")
##
##
##        while True:
##            aadhar = input ("Enter your Aadhar Number -: ")
##            print("+------------------------------------------------+")
##            if aadhar.isdigit () and len(aadhar) == 12:
##                aadhar = int (aadhar)
##                break
##            else:
##                print("Invalid Input...!\nPlease Enter Only Numbers that length should be 12...!")
##                print("+------------------------------------------------+")
##
##        acn = 0
##        aadhar1=aadhar
##        while(aadhar1>0):
##            rem = aadhar1 % 10
##            acn = acn * 10 + rem
##            aadhar1 = aadhar1//10
##        print("Your Account Successfully Created...!\nYour Account Number Is -: ",acn)
##        print("+------------------------------------------------+")
##  
##        users[name] = Bank(name,gender,mobile,salary,email,pin,aadhar)
##
##    elif choice == "2":
##        name = input("Enter Your Name -: ")
##        while True:
##            pin_input = input("Enter Your Password (PIN) -: ")
##            print("+------------------------------------------------+")
##            if pin_input.isdigit() and len(pin_input)==4:
##                pin = int(pin_input)
##                break
##            else:
##                print("Invalid PIN...\nPlease Enter a Only Numbers length Should Be 10...!")
##                print("+------------------------------------------------+")
##
##
##        obj = users.get(name,0)
##        if obj == 0:
##            print("No Match Found")
##        elif obj.getpin()==pin:
##            print("Access Granted...!")
##            while True:
##                print("+------------------------------------------------+")
##                print("1.Deposite\n2.Withdraw\n3.View Balance\n4.Transfer\n5.View Acconut Details\n6.Logout")
##                print("+------------------------------------------------+")
##                action = input("Choose And Action -: ")
##                print("+------------------------------------------------+")
##                if action == "1":
##                    while True:
##                        amount_input = input("Enter the Deposite Amount -: ")
##                        if amount_input.isdigit():
##                            amount = int(amount_input)
##                            break
##                        else:
##                            print("Invalid Amount...!\nPlease Enter Only Numbers...!")
##                            print("+------------------------------------------------+")
##                    obj.deposite(amount)
##
##                    
##                elif action == "2":
##                    while True:
##                        amount_input = input("Enter the Withdraw Amount -: ")
##                        print("+------------------------------------------------+")
##                        if amount_input.isdigit():
##                            amount = int(amount_input)
##                            break
##                        else:
##                            print("Invalid Amount...!\nPlease Enter Only Numbers...!")
##                            print("+------------------------------------------------+")
##                    obj.withdraw(amount)
##
##                    
##                elif action == "3":
##                    obj.viewbalance()
##
##                    
##                elif action == "4":
##                    accountant_name = input("Enter the Account User Name -: ")
##                    print("+------------------------------------------------+")
##                    account = User(accountant_name,0,17)
##                    if account == 0:
##                        print("Person Not Found...!")
##                    else:
##                        while True:
##                            amount = input("Enter the Transfer Amount -: ")
##                            print("+------------------------------------------------+")
##                            if amount.isdigit():
##                                amount = int(amount)
##                                break
##                            else:
##                                print("Invalid Amount...!\nPlease Enter Only Numbers...!")
##                                print("+------------------------------------------------+")
##                        obj.transfer(amount, account)
##
##                elif action == "5":
##                    obj.viewdetails()
##
##                        
##                elif action == "6":
##                    print("Logging Out...!")
##                    break
##                else:
##                    print("Invalid Operation, Try Again ...!")
##        else:
##            print("Access Denied")
##    elif choice == "3":
##        print("! --------- Thank You -------- !\n! -------- Visit Again ------- ! \n! ------------ Exit ---------- !")
##        break
                    
                        

class User():
    __count = 0  # Class variable to keep track of the number of users

    def __init__(self, name, gender, salary):
        """
        Constructor method for User class.

        Parameters:
            name (str): User's name.
            gender (str): User's gender.
            salary (int): User's salary.
        """
        self.name = name
        self.gender = gender
        self.salary = salary
        User.__count += 1
        self.__account = User.__count  # Private variable to store user account number

    def showdetails(self):
        """
        Method to display user details.
        """
        print(f"Name : {self.name}\nGender : {self.gender}\nSalary : {self.salary}")
        print("+------------------------------------------------+")
        print("Account No : ", self.__account)


class Bank():
    __balance = 0  # Class variable to store bank's balance
    __bankname = "HDFC Bank".center(30)  # Class variable to store bank's name
    __usercount = 0  # Class variable to keep track of the number of users in the bank

    def __init__(self, name, gender, mobile, salary, email, pin, aadhar):
        """
        Constructor method for Bank class.

        Parameters:
            name (str): User's name.
            gender (str): User's gender.
            mobile (str): User's mobile number.
            salary (int): User's salary.
            email (str): User's email address.
            pin (int): User's PIN (password).
            aadhar (int): User's Aadhar number.
        """
        self.name = name
        self.gender = gender
        self.mobile = mobile
        self.salary = salary
        self.email = email
        self.__pin = pin  # Private variable to store user's PIN
        self.aadhar = aadhar
        Bank.__usercount += 1

    def deposite(self, amount):
        """
        Method to deposit money into the user's account.

        Parameters:
            amount (int): Amount to be deposited.
        """
        self.__balance += amount
        print("Amount Deposited Successfully...!")
        print("+------------------------------------------------+")
        print("Your Current Balance Is -:", self.__balance)

    def withdraw(self, amount):
        """
        Method to withdraw money from the user's account.

        Parameters:
            amount (int): Amount to be withdrawn.
        """
        if amount > self.__balance:
            print("Insufficient Balance")
            print("+------------------------------------------------+")
            print("Your Current Balance Is -:", self.__balance)
        elif 100 <= amount <= self.__balance:
            self.__balance -= amount
            print("Thank You For Visiting Our Branch...!")
        elif amount < 100:
            print("You Can't Withdraw Amount Less Than 100")
            print("Your Current Balance Is -:", self.__balance)

    def viewbalance(self):
        """
        Method to view the user's account balance.
        """
        print(f"Name -: {self.name}\nGender -: {self.gender}\nCurrent Balance -: {self.__balance}")

    def viewdetails(self):
        """
        Method to view the user's account details.
        """
        print(f"Name -: {self.name}\nGender -: {self.gender}\nSalary -: {self.salary}\nCurrent Balance -: {self.__balance}\nMobile No. -: {self.mobile}")
        print("Aadhar No -: ", self.aadhar)
        print("Account No -: ", acn)

    def transfer(self, amt, user):
        """
        Method to transfer money to another user's account.

        Parameters:
            amt (int): Amount to be transferred.
            user (User): User object to transfer money to.
        """
        if amt > self.__balance:
            print("Insufficient Balance")
            print("+------------------------------------------------+")
            print("Your Current Balance Is -:", self.__balance)
        elif amt >= 1 and amt <= self.__balance:
            self.__balance -= amt
            print("Amount Transfer Successfully")
            print("+------------------------------------------------+")
            print("Your Current Balance Is -:", self.__balance)
        elif amt < 1:
            print("You Can't Transfer Amount Less Than 1")
            print("+------------------------------------------------+")
            print("Your Current Balance Is -:", self.__balance)

    def getusername(self):
        """
        Method to get user's name.
        """
        return self.name

    def getpin(self):
        """
        Method to get user's PIN.
        """
        return self.__pin

    def logindata(self):
        """
        Method to get user's login data.
        """
        return [self.name, self.__pin]

    def __str__(self):
        """
        String representation of the Bank object.
        """
        return f"{self.name} {self.__pin}"


users = {}  # Dictionary to store user objects

while True:
    print("+------------------ Wel-Come To Durgesh's Bank------------------------+")

    print("|+----------------------------------+|")
    print("| Sr.No |          Steps             |")
    print("|+----------------------------------+|")
    print("| 1.    |       Create Account       |")
    print("|+----------------------------------+|")
    print("| 2.    |          Login             |")
    print("|+----------------------------------+|")
    print("| 3.    |           Exit             |")
    print("|+----------------------------------+|")

    print("+------------------------------------------------+")
    choice = input("Enter Your Choice -: ")
    print("+------------------------------------------------+")

    print("")

    if choice == "1":
        # User account creation process
        while True:
            name = input("Enter Your Name -: ")
            print("------------------------------------------------")
            if name.isalpha():
                break
            else:
                print("Invalid Name...!\nPlease Enter Only Characters...!")
                print("------------------------------------------------")

        # Gender selection process
        while True:
            print("Select Your Gender")
            print("1.Male")
            print("2.Female")
            print("3.Other")
            print("------------------------------------------------")
            gender = input("Enter Your Choice -: ")

            if gender == '1':
                print("Male")
                gender = "Male"
                break
            elif gender == '2':
                print("Female")
                gender = "Female"
                break
            elif gender == '3':
                print("Other")
                gender = "Other"
                break
            print("------------------------------------------------")

            if gender.isdigit():
                break
            else:
                print("Invalid Choice...!\nPlease Enter Valid choice...!")
                print("+------------------------------------------------+")

        # Mobile number input process
        while True:
            mobile = input("Enter Your Mobile Number -: ")
            print("+------------------------------------------------+")
            if mobile.isdigit() and len(mobile) == 10:
                break
            else:
                print("Invalid Input...!\nPlease Enter Only Numbers that length should be 10...!")
                print("+------------------------------------------------+")

        # Salary input process
        while True:
            salary = input("Enter Your Salary -: ")
            print("------------------------------------------------")
            if salary.isdigit():
                salary = int(salary)
                break
            else:
                print("Invalid Input...\nPlease Enter Only Numbers...!")
                print("+------------------------------------------------+")

        # Email input process
        while True:
            email = input("Enter Your Email-ID -: ")
            print("+------------------------------------------------+")
            break

        # PIN (password) input process
        while True:
            pin = input("Set Your Password (PIN) -: ")
            print("+------------------------------------------------+")
            if pin.isdigit() and len(pin) == 4:
                pin = int(pin)
                break
            else:
                print("Invalid Input...!\nPlease Enter Only Numbers that length should be 4...!")
                print("+------------------------------------------------+")

        # Aadhar number input process
        while True:
            aadhar = input("Enter your Aadhar Number -: ")
            print("+------------------------------------------------+")
            if aadhar.isdigit() and len(aadhar) == 12:
                aadhar = int(aadhar)
                break
            else:
                print("Invalid Input...!\nPlease Enter Only Numbers that length should be 12...!")
                print("+------------------------------------------------+")

        acn = 0
        aadhar1 = aadhar
        while aadhar1 > 0:
            rem = aadhar1 % 10
            acn = acn * 10 + rem
            aadhar1 = aadhar1 // 10
        print("Your Account Successfully Created...!\nYour Account Number Is -: ", acn)
        print("+------------------------------------------------+")

        # Creating a new Bank object for the user and adding it to the users dictionary
        users[name] = Bank(name, gender, mobile, salary, email, pin, aadhar)

    elif choice == "2":
        # Login process
        name = input("Enter Your Name -: ")
        while True:
            pin_input = input("Enter Your Password (PIN) -: ")
            print("+------------------------------------------------+")
            if pin_input.isdigit() and len(pin_input) == 4:
                pin = int(pin_input)
                break
            else:
                print("Invalid PIN...\nPlease Enter a Only Numbers length Should Be 10...!")
                print("+------------------------------------------------+")

        # Validating user login credentials
        obj = users.get(name, 0)
        if obj == 0:
            print("No Match Found")
        elif obj.getpin() == pin:
            print("Access Granted...!")

            # Handling user actions after successful login
            while True:
                print("+------------------------------------------------+")
                print("1.Deposite\n2.Withdraw\n3.View Balance\n4.Transfer\n5.View Account Details\n6.Logout")
                print("+------------------------------------------------+")
                action = input("Choose An Action -: ")
                print("+------------------------------------------------+")
                if action == "1":
                    # Deposit money into the user's account
                    while True:
                        amount_input = input("Enter the Deposit Amount -: ")
                        if amount_input.isdigit():
                            amount = int(amount_input)
                            break
                        else:
                            print("Invalid Amount...!\nPlease Enter Only Numbers...!")
                            print("+------------------------------------------------+")
                    obj.deposite(amount)

                elif action == "2":
                    # Withdraw money from the user's account
                    while True:
                        amount_input = input("Enter the Withdraw Amount -: ")
                        print("+------------------------------------------------+")
                        if amount_input.isdigit():
                            amount = int(amount_input)
                            break
                        else:
                            print("Invalid Amount...!\nPlease Enter Only Numbers...!")
                            print("+------------------------------------------------+")
                    obj.withdraw(amount)

                elif action == "3":
                    # View user's account balance
                    obj.viewbalance()

                elif action == "4":
                    # Transfer money to another user's account
                    accountant_name = input("Enter the Account User Name -: ")
                    print("+------------------------------------------------+")
                    account = User(accountant_name, 0, 17)
                    if account == 0:
                        print("Person Not Found...!")
                    else:
                        while True:
                            amount = input("Enter the Transfer Amount -: ")
                            print("+------------------------------------------------+")
                            if amount.isdigit():
                                amount = int(amount)
                                break
                            else:
                                print("Invalid Amount...!\nPlease Enter Only Numbers...!")
                                print("+------------------------------------------------+")
                        obj.transfer(amount, account)

                elif action == "5":
                    # View user's account details
                    obj.viewdetails()

                elif action == "6":
                    # Logout
                    print("Logging Out...!")
                    break
                else:
                    print("Invalid Operation, Try Again ...!")
        else:
            print("Access Denied")
    elif choice == "3":
        # Exit the program
        print("! --------- Thank You -------- !\n! -------- Visit Again ------- ! \n! ------------ Exit ---------- !")
        break


















































































































































                
                
