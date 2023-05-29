from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine
import urllib

def get_conn(server,username,password, db_name) -> Engine:
    """
    Return connection object to the database.

    Parameters
    ----------
    server : string
        name of server to connect with
    username : string
        username for SQL Server Authentication
    password : string
        password for SQL Server Authentication
    db_name : string
        database name where table will be created

    Returns
    -------
    conn : sqlalchemy.engine.Engine
        Database connection object
    """
    conn_str = urllib.parse.quote_plus(
        'Driver={ODBC Driver 18 for SQL Server};'
        f'Server={server};'
        f'UID={username};'
        f'PWD={password};'
        f'Database={db_name};')
    conn = create_engine(
        f'mssql+pyodbc:///?odbc_connect={conn_str}',
        fast_executemany=True)
    return conn