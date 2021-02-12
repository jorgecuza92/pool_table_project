

from pool_table_Azams_words import PoolTable

# create 12 pool tables
pool_tables = []
for index in (1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

print(pool_tables)

pt = pool_tables[5]
pt.check_out()

