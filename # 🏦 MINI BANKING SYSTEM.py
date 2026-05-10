# 🏦 MINI BANKING SYSTEM 

balance = 0
print("===============================")
print("🏦 Welcome To DC Bank")
print("===============================")

print("\nChoose an option:")
print("1. 👤 Create Account")
print("2. 💰 Deposit Money")
print("3. 💸 Withdraw Money")
print("4. 📈 Check Balance")
print("5. 🧾 Transaction History")
print("6. 🚪 Exit")

choice = input("Enter Choice (1-6): ")

# 👤 CREATE ACCOUNT
if choice == "1":
    
    print("\n============================")
    print("👤 Create Account ")
    print("==============================")
    
    first_name = input("Enter First Name : ")
    
    last_name = input ("Enter Last Name : ")
    
    phone_number = input("Enter Your Phone Number : ")
    
    age = input("Enter Age : ")
    
    email = input("Enter Email Address : ")
    
    address = input("Enter House Address : ")
    
    gender = input("Enter Your Gender : ")
    
    account_type = input("Enter Your Account Type (Savings/Current ) : ")
    
    pin = input("Create a 4 Digit Pin : ")
    
    
    
    print("\n✅ Account Successfullyy Created : ")
    print("====================================")
    
    print(f"👤 Name : {first_name} {last_name}")
    print(f"📞 Phone Number : {phone_number}")
    print(f"Age : {age}")
    print(f"Email : {email}")
    print(f"Address : {address}")
    print(f"Gender : {gender}")
    print(f"Account Type : {account_type}")
    print(f"Balance : $ {balance}")
    
   # 💰  Deposit Money  
elif choice ==  "2":
    
    print("\n=======================")
    print(" 💰 Deposit Money ")
    print("==========================")
    amount = int(input("Enter Amount to deposit   : $"))
    balance = balance + amount
    print("New Balance is ",  balance )
    
    # 💸 Withdraw Money 

elif choice =="3":
    print("\n==========================")
    print(" 💸 Withdraw Money ")
    print("=========================")
    amount = int(input("Enter The Amount To Withdraw : "))
    if amount <=  balance :
            balance = balance - amount
            print(f"  $ {amount}Withdraw Successful : ")
    else:
            print("Insufficient Funds : ")
            
    # 📈 Account Balance         

elif choice =="4":
    print("\n============================")
    print("📈 Account Balance")
    print("===============================")
    print("Your Account Balanace is ", balance )
    
   # 🧾 Transaction History
   
elif choice =="5":
    print("\n==============================")
    print("🧾 Transaction History")
    print("==============================")
    
    print("No Transactions Yet : ")
    
    
    # 🚪 Exit
elif choice =="6":
    print("\n🚪 Thank You For Banking With Us")
    
    #  ❌ Invalid choice 
else:
    print("❌ Invalid Option")
    
        
   
    
                
            
        
    
    
    