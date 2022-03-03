print('Welcome to Lapo Microfaince Bank')
Trial = 3
Userpin = 1234

UserLanguage = input("E: english || Y: yoruba || I: igbo || H: hausa: ")
if UserLanguage == "E":
    print("Proceed")
while Trial != 0:
    Pin = int(input("Please enter your four digit number: "))
    if Pin != Userpin:
        Trial -= 1
        print("Wrong pin number, You have", Trial, "Trial left")
    else:
        Transactionoption = input("W: withdrawal || B: balance || F: fastrack: ") 
        if Transactionoption == "W":
            Userwithdrawal = input("Enter the amount you will like to withdraw: ")
            print(Userwithdrawal, "$ Has been withdrawn from your account")
        if Transactionoption == "B":
            Userbalance = input("Saving or Current? S/C: ")
            if Userbalance == "S":
                print("Your available balance is $100000")
        if Transactionoption == "F":
            fastrack = input("A: $1000 || B: $2000 || C: $5000 || D: $10000 || E: $15000: ")
            if fastrack == "A":
               print(fastrack, "Please take your cash", "Thank you")
            
        UserExit = input("Would you like to continue? Y/N: ")
        if UserExit == "N":
            print("Thank you for using Lapo Microfiance Bank", "Kindly take your card")
            break
        else:
            print("yes")
            #continue

