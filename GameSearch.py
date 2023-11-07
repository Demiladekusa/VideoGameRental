import sqlite3

#function to search for games by title
def search_games_by_title(database, search_term):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # Use a SQL query to search for games by title
        cursor.execute("SELECT * FROM Games WHERE title LIKE ?", ('%' + search_term + '%',))
        games = cursor.fetchall()

        conn.close()
        return games

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None

if __name__ == '__main__':
    database_name = 'MyGameRentals2.db'
    search_term = 'Game_3_1'  # Replace with the desired search term

    results = search_games_by_title(database_name, search_term)

    if results is not None:
        if results:
            for game in results:
                print(game)
        else:
            print("No games matching the search term were found.")
    else:
        print("An error occurred while searching for games.")
