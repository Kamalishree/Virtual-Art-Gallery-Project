import configparser
import os

class DBPropertyUtil:
    @staticmethod
    def get_property_string(file_name):
        config = configparser.ConfigParser()
        path = os.path.join(os.getcwd(), file_name)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Property file '{file_name}' not found.")

        config.read(path)

        try:
            driver = config.get('database', 'driver')
            server = config.get('database', 'server')
            database = config.get('database', 'database')
            trusted = config.get('database', 'trusted_connection')
        except configparser.Error as e:
            raise Exception(f"Error reading property file: {e}")

        return f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection={trusted}'
