import datetime

#Pool table model
class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = None # means null, the value does not yet exist
        self.end_time = None
        self.is_occupied = False

    def check_out(self):
        # was table already occupied? if so, DO NOT check out table
        self.start_time = datetime.datetime.now()
        self.is_occupied = True
        pass

    def check_in(self):
        self.end_time = datetime.datetime.now()
        self.is_occupied = False
        pass

    def total_time_played(self):
        return self.end_time - self.start_time # make sure to get correct difference
