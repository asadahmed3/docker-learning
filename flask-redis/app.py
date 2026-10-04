from flask import Flask
import redis
import os

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello, World. Welcome to Flask with Redis!"
my_redis = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/count")
def count():
    visits =my_redis.incr("hits")
    return f"This page has been visited {visits} times."

app.run(host='0.0.0.0', port=5000)



