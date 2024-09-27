import sqlite_backend
import mvc_exceptions as mvc_exc

class ModelSQLite(object):
    def __init__(self):
        self._item_type = "tickets"
        self._connection = sqlite_backend.connect_to_db(sqlite_backend.DB_name)
        try:
            sqlite_backend.create_table(self._connection, self._item_type)
        except sqlite_backend.OperationalError:
            print("Table {} already exists".format(self._item_type))
    
    @property
    def connection(self):
        return self._connection
    
    @property
    def item_type(self):
        return self._item_type
    
    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type
    
    def create_item(self, company, sas_ticket, msx_ticket, status, date, time):
        sqlite_backend.insert_one(self.connection, company, sas_ticket, msx_ticket, status, date, time, table_name=self.item_type)

    def read_item(self, company):
        """
        Retrieves a single item from the database based on the provided company name.

        Args:
            company (str): The name of the company to search for.

        Returns:
            dict: A dictionary representing the selected row, with column names as keys and cell values as values.

        Raises:
            mvc_exceptions.CompanyNotFound: If the specified company is not found in the table.
        """
        return sqlite_backend.select_one(self.connection, company, table_name=self.item_type)
    
    def read_items(self):
        return sqlite_backend.select_all(self.connection, table_name=self.item_type)
    
    def update_item(self, company, sas_ticket, msx_ticket, status, date, time):
        sqlite_backend.update_one(self.connection, company, sas_ticket, msx_ticket, status, date, time, table_name=self.item_type)
    
    def delete_item(self, company):
        sqlite_backend.delete_one(self.connection, company, table_name=self.item_type)
    
