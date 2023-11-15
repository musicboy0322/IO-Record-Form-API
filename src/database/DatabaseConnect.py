from dotenv import load_dotenv
import os
import pymysql

class DatabaseConnect: 
    
    def __init__(self):
        load_dotenv()

        self.db_settings = {
            "host": os.getenv('DB_HOST'),
            "port": int(os.getenv('DB_PORT')),
            "user": os.getenv('DB_USERNAME'),
            "password": os.getenv('DB_PASSWORD'),
            "db": os.getenv('DB_DATABASE')
        }
        
    def conn(self, command):
        try:
            connection = pymysql.connect(**self.db_settings);

            with connection.cursor() as cursor:

                cursor.execute(command)

                result = cursor.fetchall()

                print(result)

                return result

        except Exception as e:
            print(e)
