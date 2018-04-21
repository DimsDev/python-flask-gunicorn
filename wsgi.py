#-- How to set 2 apps in Openshift

from flask import Flask
import redis
import time
import os

application = Flask(__name__)
cache = redis.StrictRedis(host=os.environ.get("REDIS_SERVICE_HOST","NOT FOUND"),
                          port=os.environ.get("REDIS_SERVICE_PORT_REDIS","NOT_FOUND"),
                          password=os.environ.get("REDIS_PASSWORD","NOT_FOUND"),
                          db=0)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            print("{}\n".format(os.environ.get("REDIS_PASSWORD","NOT_FOUND")))
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)



@application.route("/")
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    application.run()
