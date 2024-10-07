#To do list task- 5 by HARSH RAJ

contacts ={}

while True:
    print("\nContact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit")
#option in user
    choice = input("Enter your  choice=")
    if choice == "1":
        name = input("enter the your name=")
        if name in contacts:
            print("Contact name {name} alredy exists")
        else:
            age=input("Enter  the age=")
            email=input("Enter the  email id=")
            mobile=input("Enter the mobile number=")
            contacts[name]={"age":int(age),"email":email,"mobile":mobile}
            print("contact name{name} has been created successuflly:")
#view contacts in user
    elif choice =="2":
        name=input("Enter the contact name to viwe=")
        if name in contacts:
            contact=contacts[name]
            print("Name:{name},age:{age},mobile number:{mobile}")
        else:
            print("contact not found")
    #user in Update contacts value
    elif choice=="3":
        name=input("Enter name to update contact=")
        if name in contacts:
            age=input("Enter the update age =")
            email=input("Enter the  email id=")
            mobile=input("Enter the mobile number=")
            contacts[name]={"age":int(age),"email":email,"mobile":mobile}
        else:
            print("contact not found")
#delet the contacts value 
    elif choice=="4":
        name=input("Enter the contact name to delete=")
        if name in contacts:
            del contactes[name]
            print("contact Name {name} has been deleted successfully")
        else:
            print("contact not found")
#serach the contact value
    elif choice=="5":
        serach_name=input("enter the contact name to serach=")
        found =False
        for name ,contact in contacts.items():
            if serach_name.lower() in name.lower():
                print("fount - Name {name},age {age}, Mobile number :{mobile},Email:{email")
                found=True
        if not found:
           print("No contact found with that name")
#count the contacts value
    elif choice=="6":
        print("Total contact  in your book:{len(contacts)}")
    elif choice:
        print("Good by closing the program")
        break
    else:
        print("Invalid input")

            