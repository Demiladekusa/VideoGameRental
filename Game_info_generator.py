import random
import datetime

# Define a list of game platforms, genres, and titles for random selection
platforms = ["PlayStation", "Xbox", "Nintendo", "PC","Steam","Wii","Switch"]
genres = ["Action", "Adventure", "RPG", "Sports", "Simulation","racing","puzzle","multiplayer"]
titles = ["Game_1", "Game_2", "Game_3", "Game_4", "Game_5", "Game_6", "Game_7", "Game_8", "Game_9", "Game_10"]

# Function to generate a random date
def random_date():
    start_date = datetime.date(2015, 1, 1)
    end_date = datetime.date(2022, 12, 31)
    return str(start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days)))

# Create Game_Info.txt and generate data
with open("Game_Infos.txt", "w") as file:
    file.write("ID Platform Genre Title Purchase Price £ Purchase Date Availability\n")

    for game_id in range(1, 90):
        platform = random.choice(platforms)
        genre = random.choice(genres)
        title = random.choice(titles) + f"_{game_id}"
        purchase_price = random.randint(15, 130)
        purchase_date = random_date()
        availability = "Available"

        line = f"{game_id} {platform} {genre} {title} {purchase_price} {purchase_date} {availability}\n"
        file.write(line)

print("Game_Infos.txt created with example data.")
