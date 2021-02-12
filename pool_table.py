# view all the tables


# while True:


# user prompt
print("""         Step 1: Enter 1 to view all pool table
         Step 2:Enter pool table number to reserve
         Quit: Enter quit to exit""")
customer_input = int(input('Enter 1 to begin: '))
print()

availability = '- NOT OCCUPIED'
tables = [{'table1': availability},
          {'table2': availability},
          {'table3': availability},
          {'table4': availability},
          {'table5': availability},
          {'table6': availability},
          {'table7': availability},
          {'table8': availability},
          {'table9': availability},
          {'table10': availability},
          {'table11': availability},
          {'table12': availability}]


for i in tables:
    for key, value in i.items():
        print(key, value)
        # while availability == '- NOT OCCUPIED':

# VIEW ALL TABLES
if customer_input == '1':
    for i in tables:
        for key, value in i.items():
            print(key, value)





    # OCCUPIED OR NOT?
    # if availability == 'OCCUPIED':
    #     availability =
