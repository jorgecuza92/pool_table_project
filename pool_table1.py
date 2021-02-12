# Tables
import datetime

tables = []

# POOL TABLE MODEL
class PoolTable:
    def __init__(self, table_number, availability=True):
        self.table_number = table_number
        self.availability = True
        self.minutes_played = 0
        self.start_time = None
        self.end_time = None


    def add_table(self, table_list):
        table_list.append(self)
        # for table in table_list:
        #     # print(self.availability)
        #     # print(table_list)

    def checkin(self):
        self.availability = False
        self.start_time = datetime.datetime.now()

    def checkout(self):
        self.availability = True
        self.end_time = datetime.datetime.now()

    def get_time_played(self):
        return self.end_time - self.start_time


def print_table(table_list):
    tableindex = 0
    for table in table_list:
        tableindex += 1
        print(f"TABLE {tableindex} -- Availability: {table.availability}; minutes used: {table.minutes_played}")
        


def make_list_of_twelve_tables(table_list):
    for i in range(1, 13):
        new_table = PoolTable(i)
        table_list.append(new_table)



# make_list_of_twelve_tables(tables)
# print_table(tables)

# DISPLAY MENU FOR USER
print("""
***POOL TABLE MANAGEMENT SYSTEM***
Enter 1 to view all tables
Enter 2 to assign a table
Enter 3 to check-in a table
Enter \'q\' to quit
**********************************""")

make_list_of_twelve_tables(tables)

# LOGIC PART
while True:
    choice = input('Enter a choice from the menu: ')
    if choice == '1':
        print_table(tables)
    elif choice == '2':
        print_table(tables)
        print()
        choose_table = int(input("Enter 1-12 to check-out a table: "))
        table = tables[choose_table - 1]
        tables[choose_table].checkin





    elif choice == '3':
        pass
        # check in the table
    elif choice == 'q':
        break
    else:
        print('Please enter a valid command from the menu')




# def available_pool_tables(PoolTable):
#     if table.availability == True:
#         for pool_table in tables:




