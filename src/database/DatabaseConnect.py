import configparser
import pymysql

class DatabaseConnect: 
    
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.db_settings = {
            "host": config.get('Database', 'DB_HOST'),
            "port": int(config.get('Database', 'DB_PORT')),
            "user": config.get('Database', 'DB_USERNAME'),
            "password": config.get('Database', 'DB_PASSWORD'),
            "db": config.get('Database', 'DB_DATABASE')
        }
        
    def conn_get(self, command):
        try:
            connection = pymysql.connect(**self.db_settings)

            with connection.cursor() as cursor:

                cursor.execute(command)

                result = cursor.fetchall()

                print(result)

                return result

        except Exception as e:
            print(e)
    
    def conn_other(self, command, action):
        try:
            connection = pymysql.connect(**self.db_settings)

            with connection.cursor() as cursor:

                cursor.execute(command)
                connection.commit()

                return f"{action} Successful"


        except Exception as e:
            print(e)
