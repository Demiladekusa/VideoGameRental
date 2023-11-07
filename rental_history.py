# Open the file for reading
with open('rental_history.txt', 'r') as file:
    # Print the header
    print("Game ID\tRental Date\tReturn Date\tCustomer ID")
    # Read each line from the file
    for line in file:
        # Split the line into individual elements
        values = line.strip().split()
        if len(values) == 4:
            game_id, rental_date, return_date, customer_id = values
            # Print the formatted data
            print(f"{game_id}\t{rental_date}\t{return_date}\t{customer_id}")
        else:
            print(f"Skipping line: {line.strip()} (Expected 4 values)")

