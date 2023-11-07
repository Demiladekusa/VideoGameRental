import sqlite3

# Define a function to return a game
def return_game(database, ID):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # Check if the game exists in the database
        cursor.execute("SELECT * FROM games WHERE ID = ?", (ID,))
        game = cursor.fetchone()

        if not game:
            conn.close()
            return "Invalid game ID. Please provide a valid game ID."

        # Check if the game is already available (check the availability column at index 5)
        if game[6] == "Available":
            conn.close()
            return "Game is already available and cannot be returned."

        # If the game is rented, update its availability to "Available"
        cursor.execute("UPDATE games SET availability = 'Available' WHERE ID = ?", (ID,))

        conn.commit()
        conn.close()

        return "Game returned successfully."

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "An error occurred during the return process."

# TEST CASE  return_game function
if __name__ == '__main__':
    database_name = 'MyGameRentals2.db'
    ID = 2  # Replace with a valid game ID

    result = return_game(database_name, ID)
    print(result)
