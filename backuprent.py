import sqlite3
import os  
import subscriptionManager


subscription_info = "subscription_info.txt"

# function to rent a game
def rent_game(database, customer_id, ID):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # Check if the customer exists in the database
        cursor.execute("SELECT * FROM Rentals WHERE customer_id = ?", (customer_id,))
        customer = cursor.fetchone()

        if not customer:
            conn.close()
            return "Invalid customer ID. Please provide a valid customer ID."

        # Check the customer's subscription status using the subscriptionManager
        subscriptions = subscriptionManager.load_subscriptions(subscription_info)  
        if not subscriptionManager.check_subscription(customer_id, subscriptions):
            conn.close()
            return "Customer does not have an active subscription. Rental not allowed."

        # Check the availability of the game
        cursor.execute("SELECT * FROM Games WHERE ID = ?", (ID,))
        game = cursor.fetchone()

        if not game:
            conn.close()
            return "Invalid game ID. Please provide a valid game ID."

        

        conn.commit()
        conn.close()

        return "Game rented successfully."

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "An error occurred during the rental process."

# test case
if __name__ == '__main__':
    database_name = 'MyGameRentals2.db'
    customer_id = "8749"  
    ID = 1  

    result = rent_game(database_name, customer_id, ID)
    print(result)
