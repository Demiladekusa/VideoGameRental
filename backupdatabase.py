import sqlite3
import pandas as pd

# File paths
DATABASE_FILE = "GameRental.db"
GAME_INFO_FILE = "data/Game_info.txt"  # Modify the path if needed
RENTAL_HISTORY_FILE = "data/Rental_History.txt"  # Modify the path if needed

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Define the schema and create the "Games" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Games (
        id INTEGER PRIMARY KEY,
        Platform TEXT,
        Genre TEXT,
        Title TEXT,
        PurchasePrice REAL,
        PurchaseDate DATE
    )''')

    # Create the "Rentals" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Rentals (
        id INTEGER PRIMARY KEY,
        GameID INTEGER,
        RentalDate DATE,
        ReturnDate DATE,
        CustomerID INTEGER
    )''')

    conn.commit()
    conn.close()

# Function to populate the database from GameInfo.txt
def populate_games():
    try:
        df = pd.read_csv(GAME_INFO_FILE, delimiter='\t', encoding='utf-8-sig')  # Specify 'utf-8-sig' encoding
        conn = sqlite3.connect(DATABASE_FILE)
        df.to_sql("Games", conn, if_exists='replace', index=False)
        conn.close()
    except FileNotFoundError:
        print("GameInfo file not found. Please check the file path or name.")

# Function to populate the database from RentalHistory.txt
def populate_rentals():
    try:
        df = pd.read_csv(RENTAL_HISTORY_FILE, delimiter='\t')
        conn = sqlite3.connect(DATABASE_FILE)
        df.to_sql("Rentals", conn, if_exists='replace', index=False)
        conn.close()
    except FileNotFoundError:
        print("RentalHistory file not found. Please check the file path or name.")

if __name__ == '__main__':
    create_database()
    populate_games()
    populate_rentals()
    print("Database and tables created. Data populated.")
import sqlite3
import csv
import os

# File paths
DATABASE_FILE = "MyGameRentals2.db"
GAME_INFO_FILE = "Game_info.txt"
RENTAL_HISTORY_FILE = "Rental_History.txt"

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Define the schema and create the "Games" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Games (
        id INTEGER PRIMARY KEY,
        Platform TEXT,
        Genre TEXT,
        Title TEXT,
        "Purchase Price" REAL,
        "Purchase Date" DATE
    )''')

    # Create the "Rentals" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Rentals (
        GameID INTEGER,
        RentalDate DATE,
        ReturnDate DATE,
        CustomerID INTEGER
    )''')

    conn.commit()
    conn.close()

# Function to populate the database from GameInfo.txt
def populate_games():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(GAME_INFO_FILE, 'r') as file:
        reader = csv.reader(file, delimiter='\t')  # Use '\t' as the delimiter
        next(reader)  # Skip the header row

        for row in reader:
            if len(row) != 6:
                print(f"Skipped row: {row}")
                continue

            game_id, platform, genre, title, purchase_price, purchase_date = row
            cursor.execute('INSERT INTO Games (id, Platform, Genre, Title, "Purchase Price", "Purchase Date") VALUES (?, ?, ?, ?, ?, ?)',
                           (game_id, platform, genre, title, purchase_price, purchase_date))

    conn.commit()
    conn.close()

# Function to populate the database from RentalHistory.txt
def populate_rentals():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(RENTAL_HISTORY_FILE, 'r') as file:
        reader = csv.reader(file, delimiter='\t')  # Use '\t' as the delimiter
        next(reader)  # Skip the header row

        for row in reader:
            if len(row) != 4:
                print(f"Skipped row: {row}")
                continue

            game_id, rental_date, return_date, customer_id = row
            cursor.execute("INSERT INTO Rentals (GameID, RentalDate, ReturnDate, CustomerID) VALUES (?, ?, ?, ?)",
                           (int(game_id), rental_date, return_date, int(customer_id)))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    if not os.path.isfile(DATABASE_FILE):
        create_database()
        populate_games()
        populate_rentals()
        print("Database and tables created. Data populated.")
    else:
        print("Database already exists. Skipping creation and data population.")



import sqlite3
import csv
import os

# File paths
DATABASE_FILE = "MyGameRentals2.db"
GAME_INFO_FILE = "Game_infos.txt"
RENTAL_HISTORY_FILE = "Rental_History.txt"

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Define the schema and create the "games" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS games (
        ID INTEGER PRIMARY KEY,
        platform TEXT,
        genre TEXT,
        title TEXT,
        purchase_price REAL,
        purchase_date DATE
    )''')

    # Create the "rentals" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS rentals (
        game_id INTEGER,
        rental_date DATE,
        return_date DATE,
        customer_id INTEGER
    )''')

    conn.commit()
    conn.close()

# Function to populate the database from Game_info.txt
def populate_games():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(GAME_INFO_FILE, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line by space
            values = line.strip().split()

            if len(values) != 6:
                print(f"Skipped row: {values} (Expected 6 values)")
                continue

            ID, platform, genre, title, purchase_price, purchase_date = values
            cursor.execute("INSERT INTO games (ID, platform, genre, title, purchase_price, purchase_date) VALUES (?, ?, ?, ?, ?, ?)",
                           (ID, platform, genre, title, purchase_price, purchase_date))

    conn.commit()
    conn.close()

# Function to populate the database from Rental_History.txt
def populate_rentals():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(RENTAL_HISTORY_FILE, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line by space
            values = line.strip().split()

            if len(values) != 4:
                print(f"Skipped row: {values} (Expected 4 values)")
                continue

            game_id, rental_date, return_date, customer_id = values
            cursor.execute("INSERT INTO rentals (game_id, rental_date, return_date, customer_id) VALUES (?, ?, ?, ?)",
                           (game_id, rental_date, return_date, customer_id))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    if not os.path.isfile(DATABASE_FILE):
        create_database()
        populate_games()
        populate_rentals()
        print("Database and tables created. Data populated.")
    else:
        print("Database already exists. Skipping creation and data population.")




##############################v
import sqlite3
import csv
import os

# File paths
DATABASE_FILE = "MyGameRentals2.db"
GAME_INFO_FILE = "Game_infos.txt"
RENTAL_HISTORY_FILE = "Rental_History.txt"

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Define the schema and create the "games" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS games (
        ID INTEGER PRIMARY KEY,
        platform TEXT,
        genre TEXT,
        title TEXT,
        purchase_price REAL,
        purchase_date DATE,
        availability TEXT
    )''')

    # Create the "rentals" table
    cursor.execute('''CREATE TABLE IF NOT EXISTS rentals (
        game_id INTEGER,
        rental_date DATE,
        return_date DATE,
        customer_id INTEGER
    )''')

    conn.commit()
    conn.close()

# Function to populate the database from Game_info.txt
def populate_games():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(GAME_INFO_FILE, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line by space
            values = line.strip().split()

            if len(values) != 7:
                print(f"Skipped row: {values} (Expected 7 values)")
                continue

            ID, platform, genre, title, purchase_price, purchase_date, availability = values
            cursor.execute("INSERT INTO games (ID, platform, genre, title, purchase_price, purchase_date, availability) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (ID, platform, genre, title, purchase_price, purchase_date, availability))

    conn.commit()
    conn.close()

# Function to populate the database from Rental_History.txt
def populate_rentals():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    with open(RENTAL_HISTORY_FILE, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line by space
            values = line.strip().split()

            if len(values) != 4:
                print(f"Skipped row: {values} (Expected 4 values)")
                continue

            game_id, rental_date, return_date, customer_id = values
            cursor.execute("INSERT INTO rentals (game_id, rental_date, return_date, customer_id) VALUES (?, ?, ?, ?)",
                           (game_id, rental_date, return_date, customer_id))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    if not os.path.isfile(DATABASE_FILE):
        create_database()
        populate_games()
        populate_rentals()
        print("Database and tables created. Data populated.")
    else:
        print("Database already exists. Skipping creation and data population.")

################################