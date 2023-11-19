import redis
import configparser

class RedisConnect:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('C:\settings\config.ini')
        print(config)

        self.redis_settings = {
            "host": config.get('Redis', 'REDIS_HOST'),
            "port": int(config.get('Redis', 'REDIS_PORT')),
            "db": int(config.get('Redis', 'REDIS_DB'))
        }

    def conn(self):
        try:
            redis_conn = redis.StrictRedis(host=self.redis_settings.get('host'), port=self.redis_settings.get('port'), db=self.redis_settings.get('db'))
            
        except Exception as e:
            print(e)