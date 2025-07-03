import sqlite3
import csv

# === 1. Establish database connection and create table ===


def initialize_phonebook():
    with sqlite3.connect("phonebook.db") as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS PhoneBook (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT,
                phone TEXT NOT NULL UNIQUE
            )
        ''')
        print("✅ PhoneBook table is ready.")

# === 2. Insert data from CSV ===


def insert_from_csv():
    file_path = r"C:\Users\NEK\Desktop\pygame\my.csv"  # <-- YOUR PATH
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cur.execute('''
                            INSERT INTO PhoneBook (first_name, last_name, phone)
                            VALUES (?, ?, ?)
                            ''', (row['first_name'], row['last_name'], row['phone']))
                print(
                    f"Inserted: {row['first_name']} {row['last_name']} - {row['phone']}")
            except sqlite3.IntegrityError:
                print(f"Skipping duplicate phone: {row['phone']}")
    conn.commit()
    conn.close()
    print("✅ CSV data uploaded.")

# === 3. Insert data from console ===


def insert_from_console():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name (optional): ")
    phone = input("Enter phone: ")
    try:
        cur.execute('''
                    INSERT INTO PhoneBook (first_name, last_name, phone)
                    VALUES (?, ?, ?)
                    ''', (first_name, last_name, phone))
        conn.commit()
        print("✅ Contact added successfully.")
    except sqlite3.IntegrityError:
        print("❌ Error: Phone number must be unique.")
    conn.close()

# === 4. Update data ===


def update_contact():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    phone = input("Enter phone of contact to update: ")
    new_first_name = input("Enter new first name: ")
    cur.execute('''
                UPDATE PhoneBook
                SET first_name = ?
                WHERE phone = ?
                ''', (new_first_name, phone))
    if cur.rowcount == 0:
        print("❌ No contact found with that phone.")
    else:
        print("✅ Contact updated.")
    conn.commit()
    conn.close()

# === 5. Query data with filters ===


def query_contacts():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    print("Search options:\n1) All\n2) By first name\n3) By phone")
    choice = input("Choice: ")
    if choice == '1':
        cur.execute("SELECT * FROM PhoneBook")
    elif choice == '2':
        name = input("Enter first name: ")
        cur.execute(
            "SELECT * FROM PhoneBook WHERE first_name LIKE ?", (f"%{name}%",))
    elif choice == '3':
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone = ?", (phone,))
    else:
        print("Invalid choice.")
        return
    rows = cur.fetchall()
    if rows:
        print("\n--- Contacts ---")
        for row in rows:
            print(row)
    else:
        print("No contacts found.")
    conn.close()

# === 6. Delete data by username or phone ===


def delete_contact():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    print("Delete by:\n1) First name\n2) Phone")
    choice = input("Choice: ")
    if choice == '1':
        name = input("Enter first name: ")
        cur.execute("DELETE FROM PhoneBook WHERE first_name = ?", (name,))
    elif choice == '2':
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM PhoneBook WHERE phone = ?", (phone,))
    else:
        print("Invalid choice.")
        return
    print(f"✅ Deleted {cur.rowcount} contacts.")
    conn.commit()
    conn.close()


# === 7. Main menu ===
if __name__ == "__main__":
    initialize_phonebook()

    while True:
        print("\n=== 📒 PhoneBook Menu ===")
        print("1) Upload data from CSV")
        print("2) Insert contact from console")
        print("3) Update contact")
        print("4) Query contacts")
        print("5) Delete contact")
        print("6) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")