# Initialize an empty dictionary to store contacts
contacts = {}

# Infinite loop to run the contact book app until the user chooses to exit
while True:
    print("\nContact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contacts")
    print("7. Exit")
    
    # Get user choice
    choice = input("Enter your choice: ")

    # Option 1: Create a new contact
    if choice == "1":
        name = input("Enter the contact name: ")
        if name in contacts:
            print(f"Contact with the name '{name}' already exists.")
        else:
            age = input("Enter the age: ")
            email = input("Enter the email ID: ")
            mobile = input("Enter the mobile number: ")
            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
            print(f"Contact '{name}' has been created successfully.")
    
    # Option 2: View a contact by name
    elif choice == "2":
        name = input("Enter the contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Mobile: {contact['mobile']}, Email: {contact['email']}")
        else:
            print("Contact not found.")
    
    # Option 3: Update an existing contact
    elif choice == "3":
        name = input("Enter the contact name to update: ")
        if name in contacts:
            age = input("Enter the updated age: ")
            email = input("Enter the updated email ID: ")
            mobile = input("Enter the updated mobile number: ")
            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
            print(f"Contact '{name}' has been updated successfully.")
        else:
            print("Contact not found.")
    
    # Option 4: Delete a contact
    elif choice == "4":
        name = input("Enter the contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' has been deleted successfully.")
        else:
            print("Contact not found.")
    
    # Option 5: Search for a contact by name
    elif choice == "5":
        search_name = input("Enter the contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age: {contact['age']}, Mobile: {contact['mobile']}, Email: {contact['email']}")
                found = True
        if not found:
            print("No contact found with that name.")
    
    # Option 6: Display the total number of contacts
    elif choice == "6":
        print(f"Total contacts in your book: {len(contacts)}")
    
    # Option 7: Exit the program
    elif choice == "7":
        print("Goodbye! Closing the program.")
        break
    
    # Invalid input handling
    else:
        print("Invalid input. Please enter a valid option.")

