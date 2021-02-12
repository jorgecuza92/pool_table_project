# Create Pool Table class

from datetime import datetime

pool_tables = []
fmt = '%H:%M:%S'

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.minutes_played = 0
        self.start_time = None
        self.end_time = None

    def check_out(self):
        self.start_time = datetime.now()
        self.is_occupied = True

    def check_in(self):
        self.end_time = datetime.now()
        self.is_occupied = False

    def total_time(self):
        return self.end_time - self.start_time

# Create 12 pool tables based on the class
for index in range(1, 13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

# Start menu
def display_menu():
    print("""    ************************************************************
    Welcome to the Pool Hall!!!
    1. Display Tables
    2. Check Out Table
    3. Check in Table
    ************************************************************""")

# Display the tables
def display_tables():
    for index in range(0, len(pool_tables)):
        pool_table = pool_tables[index]
        print(f"table number: {pool_table.table_number} | "
              f"Occupied: {pool_table.is_occupied} | "
              f"Check-Out: {format_time(pool_table.start_time)} | "
              f"Check-In: {format_time(pool_table.end_time)}")

# Time formatting
def format_time(dt):
    if dt == None:
        return "time not started"
    else:
        return dt.strftime(fmt)

# Functionality
while True:
    display_menu()
    choice = input("What would you like to do?: ")
    if choice == '1':
        display_tables()
    elif choice == '2':
        display_tables()
        table_checkout_index = int(input('Which table would you like to checkout?: '))
        table = pool_tables[table_checkout_index - 1]
        table.check_out()
    elif choice == '3':
        display_tables()
        print()
        table_checkin_index = int(input('Which table would you like to check-in?: '))
        table = pool_tables[table_checkin_index - 1]
        table.check_in()
        # Appending pool table stats to .txt
        play_time = table.total_time()
        formatted_play_time = str(play_time)
        with open("pool_table_stats.txt", "a") as file:
            file.write('\n\n***POOL TABLE CHECK-IN STATS***')
            file.write(f"\nPool Table Number: {table.table_number}"
                       f"\nStart Date Time: {format_time(table.start_time)}"
                       f"\nEnd Date Time: {format_time(table.end_time)}"
                       f"\nThe total time used: {formatted_play_time}")
            file.write("\n")
    elif choice == 'q':
        break
    else:
        print("Invalid input. Try again.")


