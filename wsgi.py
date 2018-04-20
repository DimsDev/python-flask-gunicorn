from flask import Flask
import redis

application = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
