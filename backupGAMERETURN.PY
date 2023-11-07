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

        # Check if the game is already available
        if game["availability"] == "Available":
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

# Example usage of the return_game function
if __name__ == '__main__':
    database_name = 'MyGameRentals2.db'
    ID = 1  # Replace with a valid game ID

    result = return_game(database_name, ID)
    print(result)








################################################################################################

import sqlite3

# Define a function to return a game
def return_game(database, customer_id, ID):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # Debug print statements
        print("Provided customer ID and game ID:", customer_id, ID)

        # Check if the game exists in the database
        cursor.execute("SELECT ID, rented_by, availability FROM games WHERE ID = ?", (ID,))
        game_info = cursor.fetchone()

        # Debug print statement
        print("Game Info:", game_info)

        if game_info is None:
            conn.close()
            return "Invalid game ID. Please provide a valid ID."

        game_id, rented_by, availability = game_info

        # Check if the customer has a valid subscription
        cursor.execute("SELECT SubscriptionType FROM subscriptions WHERE CustomerID = ?", (customer_id,))
        subscription_info = cursor.fetchone()

        if subscription_info is None:
            conn.close()
            return "Customer does not have a valid subscription."

        subscription_type = subscription_info[0]

        # Check if the customer's subscription allows them to return the game
        if subscription_type == "Basic":
            conn.close()
            return "Basic subscription does not allow game returns."

        # Check if the customer ID matches the customer who rented the game
        if rented_by == customer_id:
            if availability == 'Rented':
                cursor.execute("UPDATE games SET availability = 'Available' WHERE ID = ?", (game_id,))
                conn.commit()
                conn.close()
                return "Game returned successfully."
            else:
                conn.close()
                return "The game is already available."
        conn.close()
        return "Sorry, you cannot return this game because you did not rent it."

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "An error occurred during the return process."

# Example usage of the return_game function
if __name__ == '__main__':
    database_name = 'MyGameRentals2.db'
    customer_id = "8749"  # Replace with a valid customer ID
    ID = 2  # Replace with a valid game ID

    result = return_game(database_name, customer_id, ID)
    print(result)


################################################################################################