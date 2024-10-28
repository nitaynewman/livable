import os
import sqlite3
from typing import Dict
from dotenv import load_dotenv

load_dotenv()
# setting up db
DATABASE_FOLDER = os.getenv('DATABASE_FOLDER', './db')
DATABASE_PATH = f"{DATABASE_FOLDER}/tenant_data.db"

# creating path if not exist
def initialize_database():
    os.makedirs(DATABASE_FOLDER, exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tenant_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        property_man_comp TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# saving tenant data
def save_database(data: Dict[str, str]):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tenant_data (address, email, phone, property_man_comp)
        VALUES (:address, :email, :phone, :property_man_comp)
    ''', data)
    conn.commit()
    conn.close()

# getting mock data from the terminal while running it 
def get_data() -> Dict[str, str]:
    print("Please enter the following details:")
    address = input("Enter Address: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    property_man_comp = input("Enter Property Management Company: ")

    tenant_data = {
        "address": address,
        "email": email,
        "phone": phone,
        "property_man_comp": property_man_comp
    }
    
    print(f"Tenant data: {tenant_data}")
    return tenant_data

# retreving all the data in the db
def retrieve_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tenant_data")
    rows = cursor.fetchall()
    
    # Print each row in a readable format
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Address: {row[1]}, Email: {row[2]}, Phone: {row[3]}, Property Management Company: {row[4]}")
    else:
        print("no data found in the db.")
    
    conn.close()

def main():
    while True:
        print('''
-------------------------------------------------------------------------------------------------------------------

$$$$$$$$\                                       $$\           $$$$$$$\                       $$\               $$\ 
\__$$  __|                                      $$ |          $$  __$$\                      $$ |              $$ |
   $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$\ $$$$$$\         $$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\  $$ |
   $$ |$$  __$$\ $$  __$$\  \____$$\ $$  __$$\\_$$  _|        $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|   \____$$\ $$ |
   $$ |$$$$$$$$ |$$ |  $$ | $$$$$$$ |$$ |  $$ | $$ |          $$  ____/ $$ /  $$ |$$ |  \__| $$ |     $$$$$$$ |$$ |
   $$ |$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$ | $$ |$$\       $$ |      $$ |  $$ |$$ |       $$ |$$\ $$  __$$ |$$ |
   $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$ |$$ |  $$ | \$$$$  |      $$ |      \$$$$$$  |$$ |       \$$$$  |\$$$$$$$ |$$ |
   \__| \_______|\__|  \__| \_______|\__|  \__|  \____/       \__|       \______/ \__|        \____/  \_______|\__|

--------------------------------------------------------------------------------------------------------------------
''')
        print("1. enter data into the db")
        print("2. get data from the db")
        print("3. exit")
        choice = input("select an option 1, 2, or 3: ")
        
        if choice == "1":
            tenant_data = get_data()
            save_database(tenant_data)
            print("successfully saved 2 db.")
        
        elif choice == "2":
            print("getting the data...")
            retrieve_data()
        
        elif choice == "3":
            print("goodbye!!")
            break
        
        else:
            print("opps you didnt enter a valid option.")

# creating a data base
initialize_database()


if __name__ == "__main__":
    main()
