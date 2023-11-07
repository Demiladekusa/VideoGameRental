import random
import datetime

# Modify this list to match your game IDs
game_ids = [str(i) for i in range(1, 51)]

# Define the number of rental records you want to generate
num_rental_records = 200

# Define a start date for rental history
start_date = datetime.date(2020, 1, 1)

with open("Rental_History.txt", "w") as file:
    file.write("Game ID Rental Date Return Date Customer ID\n")

    for _ in range(num_rental_records):
        game_id = random.choice(game_ids)
        rental_date = start_date + datetime.timedelta(days=random.randint(1, 1095))  # Random rental date within 3 years
        return_date = rental_date + datetime.timedelta(days=random.randint(1, 30))  # Random return date within 30 days
        customer_id = random.randint(1000, 9999)

        file.write(f"{game_id} {rental_date.strftime('%d/%m/%Y')} {return_date.strftime('%d/%m/%Y')} {customer_id}\n")
