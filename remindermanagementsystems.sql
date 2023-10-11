import datetime
import sqlite3

# Function to create a SQLite database and table for reminders
def create_reminder_table():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY,
        username TEXT,
        date TEXT,
        subject TEXT,
        description TEXT,
        email TEXT,
        contact_no TEXT,
        sms_no TEXT,
        recurrence TEXT
    )'')

    conn.commit()
    conn.close()

# Function to save a new reminder to the database
def save_reminder(username, date, subject, description, email, contact_no, sms_no, recurrence):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO reminders (username, date, subject, description, email, contact_no, sms_no, recurrence)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (username, date, subject, description, email, contact_no, sms_no, recurrence))
    conn.commit()
    conn.close()

# Function to retrieve reminders from the database
def get_reminders(username):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reminders WHERE username = ?", (username,))
    reminders = cursor.fetchall()
    conn.close()
    return reminders

# Placeholder function for sending reminders
def send_reminder(reminder):
    # Implement logic to send reminders via email, phone call, or SMS here
    print(f"Sending reminder for: {reminder['description']} on {reminder['date']}")

# Function to set a new reminder
def set_reminder(username):
    print("\nSet a new Reminder")
    date = input("Select a Date (YYYY-MM-DD): ")
    subject = input("Subject: ")
    description = input("Add description: ")
    email = input("Email Address: ")
    contact_no = input("Contact No: ")
    sms_no = input("SMS No: ")
    recurrence = input("Recur for next (e.g., 7 Days, 5 Days): ")

    save_reminder(username, date, subject, description, email, contact_no, sms_no, recurrence)
    print("Reminder saved successfully!")

# Main program loop
if _name_ == "_main_":
    create_reminder_table()
    
    while True:
        user = login()
        if user is not None:
            break

    while True:
        home_page(user)
        choice = input("Enter your choice: ")

        if choice == "1":
            set_reminder(user)
        elif choice == "2":
            modify_reminder()
        elif choice == "6":
            reminders = get_reminders(user)
            if reminders:
                for reminder in reminders:
                    send_reminder(reminder)
            else:
                print("No reminders found.")
        elif choice == "7":
            print("You have been logged out. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")