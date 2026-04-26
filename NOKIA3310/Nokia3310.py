phonebookmenu = """
1. Search 
2. Search nos 
3. Add Name 
4. Erase 
5. Edit 
6. Assign tone 
7. Send b'card 
8. options 

"""

phoneoptions = """
1. Type of view 
2. Memory status 


"""

menumessages = """
1.Write messages 
2. Inbox 
3. Outbox 
4. Picture Message 
5. Templates 
6. Smileys 
7. Messages settings 

"""

messagesettings = """
1.Message center number 
2. Message sent as 
3. Message validity 
4. Delivery report 

"""

callregisters = """
1.Missed calls 
2. Received calls 
3. Dialled Numbers 
4. Erase recent call list 
5. Show call duration 
6. Show call cost 
7. Call cost setting 


"""

callduration = """
1.Last call duration 
2. All call duration 
3. Received call duration 
4. Dialled call duration 
5. Clear timers 


"""

callcost = """
1.Last call costs 
2. All call cost 
3. Clear counters 


"""

callcostsetting = """
1.Call cost limit 
2. Show costs in 


"""

tonesettings = """
1. Ringing tone 
2. Ringing volume 
3. Incoming call alert 


"""

menusettings = """
1. Call setting 
2. Phone setting 
3. Security setting 


"""

clockmenu = """
1. Alarm clock 
2. Clock settings 
3. Date settings 


"""



while true:
    print("\n MENU ")
    print("1.  Phone book")
    print("2.  Messages")
    print("3.  Chat")
    print("4.  Call register")
    print("5.  Tones")
    print("6.  Settings")
    print("7.  Call divert")
    print("8.  Games")
    print("9.  Calculator")
    print("10. Reminders")
    print("11. Clock")
    print("12. Profiles")
    print("13. SIM services")
    print("0.  Exit")

    option = input("\nEnter a number: ")
    if option == "1":
        print("\n-- Phone book --")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b'card")
        print("8. Options")
        print("9. Speed dials")
        print("10. Voice tags")
        sub_option= input("Enter a number: ")

        if sub_option== "1":
            print("Searching contacts...")
        elif sub_option == "2":
            print("Service numbers...")
        elif sub_option == "3":
            name = input("Enter name to add: ")
            print(f"'{name}' added to phonebook")
        elif sub_option == "4":
            name = input("Enter name to erase: ")
            print(f"'{name}' erased!")
        elif sub_option == "5":
            print("Edit contact...")
        elif sub_option == "6":
            print("Assign tone to contact...")
        elif sub_option == "7":
            print("Send business card...")
        elif sub_option == "8":
            print("\n-- Options --")
            print("1. Type of view")
            print("2. Memory status")
            sub_option2 = input("Enter choice: ")
            if sub_option2 == "1":
                print("Type of view selected...")
            elif suboption2 == "2":
                print("Memory status: 50/250 used")
        elif sub == "9":
            print("Speed dials...")
        elif sub == "10":
            print("Voice tags...")

    elif option == "2":
        print("\n-- Messages --")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        sub_option = input("Enter a number: ")

        if sub_option == "1":
            msg = input("Write your message: ")
            print("write message")
        elif sub_option == "2":
            print("Inbox...")
        elif sub_option == "3":
            print("Outbox...")
        elif sub_option == "4":
            print("Picture messages...")
        elif sub_option == "5":
            print("Templates...")
        elif sub_option == "6":
            print("Smileys: ")
        elif sub_option == "7":
            print("\n-- Message settings --")
            print("1. Set 1")
            print("2. Common")
            sub_option2 = input("Enter a number: ")
            if sub_option2 == "1":
                print("\n-- Set 1 --")
                print("1. Message centre number")
                print("2. Messages sent as")
                print("3. Message validity")
                sub3 = input("Enter choice: ")
                if sub_option3 == "1":
                    print("Message centre number...")
                elif sub_optin3 == "2":
                    print("Messages sent as...")
                elif sub_option3 == "3":
                    print("Message validity...")
            elif sub_option2 == "2":
                print("\n-- Common --")
                print("1. Delivery reports")
                print("2. Reply via same centre")
                print("3. Character support")
                sub_option3 = input("Enter a number: ")
                if sub_option3 == "1":
                    print("Delivery reports ON/OFF...")
                elif sub_option3 == "2":
                    print("Reply via same centre ON/OFF...")
                elif sub_option3 == "3":
                    print("Character support...")
        elif sub_option == "8":
            print("Info service...")
        elif sub_option == "9":
            print("Voice mailbox number...")
        elif sub_option == "10":
            print("Service command editor...")

   
    elif option == "3":
        print("\n Chat")

   
    elif option == "4":
        print("\n-- Call register --")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call costs")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        sub_option = input("Enter a number: ")

        if sub_option == "1":
            print("Missed calls...")
        elif sub_option == "2":
            print("Received calls...")
        elif sub_option == "3":
            print("Dialled numbers...")
        elif sub_option == "4":
            print("Recent call lists erased!")
        elif sub_option == "5":
            print("\n-- Show call duration --")
            print("1. Last call duration")
            print("2. All calls' duration")
            print("3. Received calls' duration")
            print("4. Dialled calls' duration")
            print("5. Clear timers")
            sub_option2 = input("Enter a number: ")
            if sub_option2 == "1":
                print("Last call duration...")
            elif sub_option2 == "2":
                print("All calls duration...")
            elif sub_option2 == "3":
                print("Received calls duration...")
            elif sub_option2 == "4":
                print("Dialled calls duration...")
            elif sub_option2 == "5":
                print("Clear timer...")
        elif sub_option == "6":
            print("\n Show call costs ")
            print("1. Last call cost")
            print("2. All calls' cost")
            print("3. Clear counters")
            sub_option2 = input("Enter a number: ")
            if sub_option2 == "1":
                print("Last call cost...")
            elif sub_option2 == "2":
                print("All calls cost...")
            elif sub_option2 == "3":
                print("Counters cleared!")
        elif option == "7":
            print("\nCall cost settings")
            print("1. Call cost limit")
            print("2. Show costs in")
            sub_option2 = input("Enter a number: ")
            if sub_option2 == "1":
               print("Call cost limit")
            elif sub2 == "2":
                print("Show costs in..")
        elif sub == "8":
            print("Prepaid credit...")


    elif option == "5":
        print("\nTones")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Composer")
        print("5. Message alert tone")
        print("6. Keypad tones")
        print("7. Warning and game tones")
        print("8. Vibrating alert")
        print("9. Screen saver")
        sub_option = input("Enter a number: ")

        if sub_option == "1":
            print("ringing tone...")
        elif sub_option == "2":
            print("Ringing volume")
        elif sub_option == "3":
            print("Incoming call alert...")
        elif sub_option == "4":
            print("Composer...")
        elif sub_option == "5":
            print("Message alert tone...")
        elif sub_option == "6":
            print("Keypad tones...")
        elif sub_option == "7":
            print("Warning and game tones...")
        elif sub_option == "8":
            print("Vibrating alert...")
        elif sub_option == "9":
            print("Screen saver settings...")

 
    elif option == "6":
        print("\nSettings")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")
        sub_option= input("Enter a number: ")

        if sub_option == "1":
            print("\n Call settings ")
            print("1. Automatic redial")
            print("2. Speed dialling")
            print("3. Call waiting options")
            print("4. Own number sending")
            print("5. Phone line in use")
            print("6. Automatic answer")
            sub_option2 = input("Enter a number: ")
            if sub_option2 == "1":
                print("Automatic redial...")
            elif sub_option2 == "2":
                print("Speed dialling...")
            elif sub_option2 == "3":
                print("Call waiting options...")
            elif sub_option2 == "4":
                print("Own number sending...")
            elif sub_option2 == "5":
                print("Phone line in use...")
            elif sub_option2 == "6":
                print("Automatic answer ON/OFF...")

        elif sub_option == "2":
            print("\n-- Phone settings --")
            print("1. Language")
            print("2. Cell info display")
            print("3. Welcome note")
            print("4. Network selection")
            print("5. Lights")
            print("6. Confirm SIM service actions")
            sub_option2 = input("Enter a number: ")
            if sub_option2 == "1":
                print("Language...")
            elif sub_option2 == "2":
                print("Cell info display...")
            elif sub_option2 == "3":
                print("Welcome note")
            elif sub_option2 == "4":
                print("Network selection...")
            elif sub_option2 == "5":
                print("Lights...")
            elif sub_option2 == "6":
                print("Confirm SIM service actions...")

        elif sub_option == "3":
            print("\n Security settings")
            print("1. PIN code request")
            print("2. Call barring service")
            print("3. Fixed dialling")
            print("4. Closed user group")
            print("5. Phone security")
            print("6. Change access codes")
            sub_option2 = input("Enter a number: ")
            if sub_option2 == "1":
                print("PIN code request...")
            elif sub_option2 == "2":
                print("Call barring service...")
            elif sub_option2 == "3":
                print("Fixed dialling...")
            elif sub_option2 == "4":
                print("Closed user group...")
            elif sub_option2 == "5":
                print("Phone security...")
            elif sub_option2 == "6":
                print("Change access codes")

        elif sub_option == "4":
                print("Factory settings restored!")
            else:
                print("Cancelled.")

   
    elif option == "7":
        print("\n Call divert")
        

    elif option == "8":
        print("\n-- Games --")
        

    elif option == "9":
        print("\n-- Calculator --")
        


    elif option == "10":
        print("\n-- Reminders --")
       

    elif option == "11":
        print("\n-- Clock --")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date setting")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")
        sub_option = input("Enter a number: ")

        if sub_option == "1":
            print("Alarm")
        elif sub_ption == "2": 
           print("Clock setting")
        elif sub_option == "3":
            print("Date setting")
        elif sub_opton == "4":
            print("Stopwatch")
        elif suboption == "5":
            print("Countdown timer")
        elif sub_option == "6":
            print("Auto update of date and time...")

   
    elif option == "12":
        print("\n Profiles")
        print("1. General")
        print("2. Silent")
        print("3. Meeting")
        print("4. Outdoor")
        print("5. Pager")
        sub_option = input("Enter a number: ")
        if sub_option == "1":
            print("General")
        elif sub_opton == "2":
            print("Silent")
        elif sub_option == "3":
            print("Meeting")
        elif sub_option == "4":
            print("Outdoor")
        elif sub_option == "5":
            print("Pager")

   
    elif option == "13":
        print("\n SIM services")
        print("This feature depends on your SIM card.")
        print("Contact your network provider for details.")

    
    elif choice == "0":
        print("\nGoodbye! 👋")
        break

    else:
        print("Invalid choice! Please try again.")
