#importing modules needed
import sqlite3
import csv
import os

# different File paths used for the databse
DATABASE_FILE = "MyGameRentals2.db"
GAME_INFO_FILE = "Game_infos.txt"
RENTAL_HISTORY_FILE = "Rental_History.txt"
SUBSCRIPTIONS_FILE = "subscription_info.txt"  

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    #  creating the "games" table schema for database
    cursor.execute('''CREATE TABLE IF NOT EXISTS games (
        ID INTEGER PRIMARY KEY,
        platform TEXT,
        genre TEXT,
        title TEXT,
        purchase_price REAL,
        purchase_date DATE,
        availability TEXT
    )''')

    # Creating the "rentals" table schema for database
    cursor.execute('''CREATE TABLE IF NOT EXISTS rentals (
        game_id INTEGER,
        rental_date DATE,
        return_date DATE,
        customer_id INTEGER
    )''')

    # Creating the "subscriptions" table schema for database
    cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions (
        CustomerID INTEGER PRIMARY KEY,
        SubscriptionType TEXT,
        StartDate DATE,
        EndDate DATE
    )''')

    conn.commit()
    conn.close()

# Function to populate the database using Game_info.txt
def populate_games():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(GAME_INFO_FILE, 'r') as file:
        # Read each line from the file
        for line in file:
            
            values = line.strip().split()
            # a form of error handling ensuring the table is right format 
            if len(values) != 7:
                print(f"Skipped row: {values} (Expected 7 values)")
                continue

            ID, platform, genre, title, purchase_price, purchase_date, availability = values
            cursor.execute("INSERT INTO games (ID, platform, genre, title, purchase_price, purchase_date, availability) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (ID, platform, genre, title, purchase_price, purchase_date, availability))

    conn.commit()
    conn.close()

# Function to populate the database using Rental_History.txt
def populate_rentals():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(RENTAL_HISTORY_FILE, 'r') as file:
        # Read each line from the file
        for line in file:
            
            values = line.strip().split()

            if len(values) != 4:
                print(f"Skipped row: {values} (Expected 4 values)")
                continue

            game_id, rental_date, return_date, customer_id = values
            cursor.execute("INSERT INTO rentals (game_id, rental_date, return_date, customer_id) VALUES (?, ?, ?, ?)",
                           (game_id, rental_date, return_date, customer_id))

    conn.commit()
    conn.close()

# Function to populate the database using subscription_info.txt
def populate_subscriptions():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(SUBSCRIPTIONS_FILE, 'r') as file:
        # Read the CSV data from subscription_info.txt
        reader = csv.DictReader(file)
        for row in reader:
            # Extract values from each row
            CustomerID = int(row['CustomerID'])
            SubscriptionType = row['SubscriptionType']
            StartDate = row['StartDate']
            EndDate = row['EndDate']

            cursor.execute("INSERT INTO subscriptions (CustomerID, SubscriptionType, StartDate, EndDate) VALUES (?, ?, ?, ?)",
                           (CustomerID, SubscriptionType, StartDate, EndDate))

    conn.commit()
    conn.close()
    
# test case for function 
if __name__ == '__main__':
    if not os.path.isfile(DATABASE_FILE):
        create_database()
        populate_games()
        populate_rentals()
        populate_subscriptions()  # Call the function to populate subscriptions
        print("Database and tables created. Data populated.")
    else:
        print("Database already exists. Skipping creation and data population.")





