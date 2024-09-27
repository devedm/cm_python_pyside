import sqlite3
from sqlite3 import OperationalError, IntegrityError, ProgrammingError
import mvc_exceptions as mvc_exc


DB_name = "tickets_database"

def connect_to_db(db=None):
    """Connect to a sqlite DB. Create the database if there isn't one yet.

    Open a connection to a SQLite DB (either a DB file or an in-memory DB).
    When a database is accessed by multiple connections, and one of the
    processes modifies the database, the SQLite database is locked until that
    transaction is committed.

    Parameters
    ----------
    db : str
        database name (without .db extension). If None, create an In-Memory DB.

    Returns
    -------
    connection : sqlite3.Connection
        connection object
    """

    if db is None:
        mydb = ':memory:'
        print("New connection to In-Memory DB...")
    else:
        mydb = '{}.db'.format(db)
        print("New connection to {}...".format(mydb))
    connection = sqlite3.connect(mydb)
    return connection
    
# TODO: use this decorator to wrap commit/rollback in a try/except block ?
# see https://www.kylev.com/2009/05/22/python-decorators-and-database-idioms/
def connect(func):
    """Decorator to (re)open a sqlite database connection when needed.

    A database connection must be open when we want to perform a database query
    but we are in one of the following situations:
    1) there is no connection
    2) the connection is closed

    Parameters
    ----------
    func : function
        function which performs the database query

    Returns
    -------
    inner func : function
    """
    def inner_func(conn, *args, **kwargs):
        try:
            # I don't know if this is the simplest and fastest query to try
            conn.execute('SELECT name FROM sqlite_temp_master WHERE type="table";')
        except (AttributeError, ProgrammingError):
            conn = connect_to_db(DB_name)
        return func(conn, *args, **kwargs)
    return inner_func

def disconnect_from_db(db=None, conn=None):
    if db is not DB_name:
        print("Closing connection to {}...".format(db))
    if conn is not None:
        conn.close()

def scrub(input_string):
    """Clean an input string (to prevent SQL injection).

    Parameters
    ----------
    input_string : str

    Returns
    -------
    str
    """
    return ''.join(k for k in input_string if k.isalnum())

@connect
def create_table(conn, table_name):
    """
    Creates a table in the database.

    Parameters:
        conn (sqlite3.Connection): The SQLite database connection.
        table_name (str): The name of the table to be created.

    Returns:
        None
    """
    table_name = scrub(table_name)
    sql = 'CREATE TABLE {} (rowid INTEGER PRIMARY KEY AUTOINCREMENT, company TEXT UNIQUE, sas_ticket TEXT, msx_ticket TEXT, status TEXT, date TEXT, time TEXT)'.format(table_name)
    try:
        conn.execute(sql)
    except OperationalError as e:
        print("Error creating table: {}".format(e))


@connect
def insert_one(conn, company, sas_ticket, msx_ticket, status, date, time, table_name):
    table_name = scrub(table_name)
    sql = 'INSERT INTO {} (company, sas_ticket, msx_ticket, status, date, time) VALUES (?, ?, ?, ?, ?, ?)'.format(table_name)
    try:
        conn.execute(sql, (company, sas_ticket, msx_ticket, status, date, time))
        conn.commit()
    except IntegrityError as e:
        raise mvc_exc.CompanyAlreadyStored('{}: "{}" already stored in table "{}"'.format(e, company, table_name))

def tuple_to_dict(mytuple):
    mydict = dict()
    mydict['id'] = mytuple[0]
    mydict['company'] = mytuple[1]
    mydict['sas_ticket'] = mytuple[2]
    mydict['msx_ticket'] = mytuple[3]
    mydict['status'] = mytuple[4]
    mydict['date'] = mytuple[5]
    mydict['time'] = mytuple[6]
    return mydict

@connect
def select_one(conn, company, table_name):
    """
    Executes a SELECT query on the specified table with the given company name.

    Parameters:
        conn (sqlite3.Connection): The SQLite database connection.
        table_name (str): The name of the table to query.
        company (str): The name of the company to search for.

    Returns:
        dict: A dictionary representing the selected row, with column names as keys and cell values as values.

    Raises:
        mvc_exceptions.CompanyNotFound: If the specified company is not found in the table.
    """
    sql = f'SELECT * FROM {table_name} WHERE company="{company}"'
    c = conn.execute(sql)
    result = c.fetchone()
    if result is not None:
        return tuple_to_dict(result)
    else:
        raise mvc_exc.CompanyNotFound('Can\'t read "{}" because it\'s not stored in table "{}"'.format(company, table_name))

@connect
def select_all(conn, table_name):
    table_name = scrub(table_name)
    sql = 'SELECT * FROM {}'.format(table_name)
    c = conn.execute(sql)
    results = c.fetchall()
    return list(map(lambda x: tuple_to_dict(x), results))

@connect
def update_one(conn, table_name, company, sas_ticket, msx_ticket, status, date, time):
    table_name = scrub(table_name)
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE company=? LIMIT 1)'.format(table_name)
    sql_update = 'UPDATE {} SET sas_ticket=?, msx_ticket=?, status=?, date=?, time=? WHERE company=?'.format(table_name)
    c = conn.execute(sql_check, (company,)) # the coma is needed
    result = c.fetchone()
    if result[0]:
        c.execute(sql_update, (sas_ticket, msx_ticket, status, date, time, company))
        conn.commit()
    else:
        raise mvc_exc.CompanyNotFound(
            'Can\'t update "{}" because it\'s not stored in table "{}"'.format(company, table_name))

@connect
def delete_one(conn, company , table_name):
    table_name = scrub(table_name)
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE company=? LIMIT 1)'.format(table_name)
    table_name = scrub(table_name)
    sql_delete = 'DELETE FROM {} WHERE company=?'.format(table_name)
    c = conn.execute(sql_check, (company,)) # the coma is needed
    result = c.fetchone()
    if result[0]:
        c.execute(sql_delete, (company,))
        conn.commit()
    else:
        raise mvc_exc.CompanyNotFound(
            'Can\'t delete "{}" because it\'s not stored in table "{}"'.format(company, table_name))

# def main():
#     my_table_name = 'tickets'
#     conn = connect_to_db(DB_name)

#     create_table(conn, my_table_name)

#     # Create
#     insert_one(conn, table_name='tickets', company='Company1', sas_ticket='SAS Ticket 1', msx_ticket='MSX Ticket 1', status='PTC', date='01/01/2024', time='12:00:00')
#     insert_one(conn, table_name='tickets', company='Company2', sas_ticket='SAS Ticket 2', msx_ticket='MSX Ticket 2', status='PTC', date='02/01/2024', time='10:00:00')
#     # if we try to insert an object already stored we get an ItemAlreadyStored
#     # exception
#     # insert_one(conn, 'milk', price=1.0, quantity=3, table_name='items')

#     # Read
#     print('SELECT Company1')
#     print(select_one(conn, table_name='tickets', company='Company 1'))
#     print('SELECT all')
#     print(select_all(conn, table_name='tickets'))
#     # if we try to select an object not stored we get an ItemNotStored exception
#     # print(select_one(conn, 'pizza', table_name='items'))

#     # conn.close()  # the decorator @connect will reopen the connection

#     # Update
#     print('UPDATE Company1, SELECT Company1')
#     update_one(conn, table_name='tickets', sas_ticket='SAS Ticket 1', msx_ticket='MSX Ticket 1', status='Install', date='01/01/2021', time='12:00:00', company='Company1')
#     print(select_one(conn, table_name='tickets', company='Company1'))
#     # if we try to update an object not stored we get an ItemNotStored exception
#     # print('UPDATE pizza')
#     # update_one(conn, 'pizza', price=1.5, quantity=5, table_name='items')

#     # Delete
#     print('DELETE Company1, SELECT all')
#     delete_one(conn, table_name='tickets', company='Company1')
#     print(select_all(conn, table_name='tickets'))

#     # save (commit) the changes
#     conn.commit()

#     # close connection
#     conn.close()

# if __name__ == '__main__':
#     main()