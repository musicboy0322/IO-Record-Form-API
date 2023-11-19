import redis
from dotenv import load_dotenv
import os

class RedisConnect:

    def __init__(self):
        load_dotenv('C:/settings/.env')

        self.redis_settings = {
            "host": os.getenv('REDIS_HOST'),
            "port": int(os.getenv('REDIS_PORT')),
            "db": int(os.getenv('REDIS_DB'))
        }

    def conn(self):
        try:
            redis_conn = redis.StrictRedis(host=self.redis_settings.get('host'), port=self.redis_settings.get('port'), db=self.redis_settings.get('db'))
            
        except Exception as e:
            print(e)