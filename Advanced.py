import time
print("Welcome To Kartikey's Bank")
time.sleep(2)
password = '9898'



pin = input("Enter your Pin")
available = 5000

if pin == password:
   time.sleep(1)
   while True:
        print("1.)Balance Inquiry",
              "\n2.)Withdraw",
              "\n3.)Change Pin",
              "\n4.)Deposit"
              "\n5.)Quit")


        choice = input("enter Your choice")

        if choice == '1':
            time.sleep(1)
            print(f"Balance is {available}")

        elif choice == '2':

                amount = int(input("Enter the amount"))
                if amount>=1:
                    if amount <= available:
                        print(f"Debited {amount} from your account")
                        available = available - amount
                    else:
                        print("Insufficent Balance")
                else:
                    print("Enter Positive Amount")
        elif choice == '3':
            pass

        elif choice == '4':
            time.sleep(2)
            print("Please Place the Cash in the Tray For Deposit")
            time.sleep(1)
            print("Please Wait ATM is Counting The Cash.")

            deposit = int(input("Please Give the Amount Placed in the Tray"))
            time.sleep(1)
            try:
                if deposit >= 1 and deposit <=10000:
                    available = available + deposit
                    print(f"Updated Amount is {available}.")
                elif deposit == 0 :
                    print("Can't be Zero")
                else:
                    print("Dear Customer, your Range of Deposit is upto 10000.")
            except ValueError:
                print("Enter Correct Format")


        elif choice == '5':
            print("Thanks for Using Kartikey's Atm..!")
            break

else:
    print("Incorrect Pin")
