import GameSearch
import GameRent
import GameReturn

#  function to display the menu and handle different user input
def main_menu():
    while True:
        print("\n***  Game Rental  Menu ***")
        print("1. Search for a game")
        print("2. Rent a game")
        print("3. Return a game")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            search_term = input("Enter a search term: ")
            results = GameSearch.search_games_by_title("MyGameRentals2.db", search_term)  
            if results is not None:
                if results:
                    for game in results:
                        print(game)
                else:
                    print("No games matching the search term were found.")
            else:
                print("An error occurred while searching for games.")

        elif choice == "2":
            customer_id = input("Enter your customer ID: ")
            ID = input("Enter the game ID to rent: ")
            result = GameRent.rent_game("MyGameRentals2.db", customer_id, ID)  # Pass the database name
            print(result)

        elif choice == "3":
            ID = input("Enter the game ID to return: ")
            result = GameReturn.return_game("MyGameRentals2.db", ID)  # Pass the database name
            print(result)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()

