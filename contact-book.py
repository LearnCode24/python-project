contact_book={}

while True:
    print(f"""======Contact-Book======
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit
""")
    choice=int(input("Enter your choice from above list:"))
    if choice==1:
        print("======Add Contacts======")
        name=input("Enter the name : ").capitalize()
        phone_number=input("Enter the phone number :")
        email=input("Enter the email : ").lower()
        contact_book[name ]= {"Phone Number":phone_number,"Email":email}
        print("Details added successfully")
    elif choice==2:
        print("======Search Contacts======")
        name=input("Enter the name you wanna search in contacts: ").capitalize()
        print(contact_book.get(name ,f"{name} is not found in contacts!"))
    elif choice==3:
        print("======Update Contacts======")
        name=input("Enter the name you wanna update : ").capitalize()
        if name not in contact_book:
            print(f"{name} is not found in contact, you can add by choosing option 1")
        else:
            print(contact_book[name])
            print("""What you wanna update :
        1.Phone Number
        2.Email""")
            choose=int(input("Enter your choice :"))
            if choose==1:
                phone_number=input("Enter the new phone number:")
                contact_book[name]["Phone Number"]=phone_number
                print("Phone Number updated successfully!")
                print(contact_book)
            elif choose==2:
                email=input("Enter the new email:").lower()
                contact_book[name]["Email"]=email
                print("Email updated successfully!")
                print(contact_book)
            else:
                print("Invalid input!")
    elif choice==4:
        print("=====Delete Contact=====")
        name=input("Enter the name you wanna delete:").capitalize()
        if name not in contact_book:
            print(f"{name} is not found in contact, you can add by choosing option 1")
        else:
            del contact_book[name]
            print(f"{name} is deleted successfully!")
    elif choice==5:
        print("====View Contacts=====")
        for name,details in contact_book.items():
            print(f"""======Contacts======
                        Name:{name}
                        Phone Number:{details["Phone Number"]}
                        Email:{details["Email"]}""")
            
    elif choice==6:
        print("Exiting...")
        break