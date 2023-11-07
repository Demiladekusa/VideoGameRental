import sqlite3
import subscriptionManager

subscription_info = "subscription_info.txt"

# Function to rent a game
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

        # Check if the customer has rented any games
        cursor.execute("SELECT * FROM Rentals WHERE customer_id = ? AND game_id = ?", (customer_id, ID))
        rented_game = cursor.fetchone()

        if rented_game:
            conn.close()
            return "You have already rented this game."

        # Check the customer's subscription status using the subscriptionManager
        subscriptions = subscriptionManager.load_subscriptions(subscription_info)

        if not subscriptionManager.check_subscription(customer_id, subscriptions):
            conn.close()
            return "Customer does not have an active subscription. Rental not allowed."

        # Check if the customer has an active subscription type
        cursor.execute("SELECT SubscriptionType FROM subscriptions WHERE CustomerID = ?", (customer_id,))
        subscription_type = cursor.fetchone()

        if not subscription_type:
            conn.close()
            return "Customer does not have a valid subscription type."

        # Get the rental limit based on the customer's subscription type
        rental_limit = subscriptionManager.get_rental_limit(subscription_type[0])

        # Check how many games the customer has rented
        cursor.execute("SELECT COUNT(*) FROM Rentals WHERE customer_id = ?", (customer_id,))
        num_rented_games = cursor.fetchone()[0]

        if num_rented_games >= rental_limit:
            conn.close()
            return f"Sorry, you have reached your rental limit based on your subscription (SubscriptionType: {subscription_type[0]})."

        # Update the game table  availability  coulumn to "unavailable" to corresponding ID
        cursor.execute("UPDATE games SET availability = ? WHERE ID = ?", ("unavailable", ID))

        conn.commit()
        conn.close()

        return f"Game rented successfully. You can still rent {rental_limit - num_rented_games} more games."

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "An error occurred during the rental process."

# test case
if __name__ == '__main__':
    database_name = 'MyGameRentals2.db'
    customer_id = "8749"
    ID = 2

    result = rent_game(database_name, customer_id, ID)
    print(result)
