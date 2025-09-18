import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                conn_str = DBPropertyUtil.get_property_string('db.properties')
                DBConnection.connection = pyodbc.connect(conn_str)
            except Exception as e:
                print("Error while connecting to database:", e)
                raise e
        return DBConnection.connection
