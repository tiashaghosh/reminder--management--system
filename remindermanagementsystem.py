remindermanagementsystem
import datetime

# Mock database for reminders
reminders = []

# Function to display the home page
def home_page(username):
    today = datetime.date.today()
    print(f"Welcome to the Reminder Application {username}")
    print(f"Today is {today.strftime('%A, %dth Of %B')}")
    print("\n1. Set Reminder")
    print("2. Modify Reminder")
    print("3. Disable Reminder")
    print("4. Delete Reminder")
    print("5. Enable Reminder")
    print("6. View your Reminders")
    print("7. Log out")

# Function to display login page
def login():
    username = input("Username: ")
    password = input("Password: ")

    # Check credentials (implement actual login logic)
    if username == "your_username" and password == "your_password":
        return username
    else:
        print("Login Failed")
        return None

# Function to set a new reminder
def set_reminder():
    print("\nSet a new Reminder")
    date = input("Select a Date (YYYY-MM-DD): ")
    subject = input("Subject: ")
    description = input("Add description: ")
    email = input("Email Address: ")
    contact_no = input("Contact No: ")
    sms_no = input("SMS No: ")
    recurrence = input("Recur for next (e.g., 7 Days, 5 Days): ")

    # Store the reminder in the database (implement database logic)
    reminders.append({
        'date': date,
        'subject': subject,
        'description': description,
        'email': email,
        'contact_no': contact_no,
        'sms_no': sms_no,
        'recurrence': recurrence
    })
    print("Reminder saved successfully!")

# Function to display the Modify Reminder page
def modify_reminder():
    print("\nModify Reminder")
    date = input("Select Date (YYYY-MM-DD): ")
    subject = input("Select Subject: ")
    
    # Fetch reminders based on date and subject (implement database logic)
    matching_reminders = [reminder for reminder in reminders if reminder['date'] == date and reminder['subject'] == subject]

    if not matching_reminders:
        print("No matching reminders found.")
        return

    # Display the reminders for modification
    for i, reminder in enumerate(matching_reminders):
        print(f"{i + 1}. {reminder['description'][:30]}")

    choice = int(input("Select a reminder to modify: ")) - 1
    selected_reminder = matching_reminders[choice]

    # Display reminder details and allow modification (implement logic)
    print("\nReminder Details:")
    print(f"Date: {selected_reminder['date']}")
    print(f"Subject: {selected_reminder['subject']}")
    print(f"Description: {selected_reminder['description']}")
    print(f"Email Address: {selected_reminder['email']}")
    print(f"Contact No: {selected_reminder['contact_no']}")
    print(f"SMS No: {selected_reminder['sms_no']}")
    print(f"Recurrence: {selected_reminder['recurrence']}")

    # Allow modification of fields as needed

# Main program loop
if _name_ == "_main_":
    while True:
        user = login()
        if user is not None:
            break

    while True:
        home_page(user)
        choice = input("Enter your choice: ")

        if choice == "1":
            set_reminder()
        elif choice == "2":
            modify_reminder()
        elif choice == "7":
            print("You have been logged out. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
