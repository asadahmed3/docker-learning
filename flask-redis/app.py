from flask import Flask
import redis
import os

# Read connection settings supplied by Compose.
# If they are absent, use the Redis service name and its default port.
redis_host = os.environ.get('REDIS_HOST', 'redis')

# Environment variables are text, so convert the port to an integer.
redis_port = int(os.environ.get('REDIS_PORT', 6379))

# Create the Flask application. __name__ helps Flask locate its resources.
app = Flask(__name__)

# Configure a client for the separate Redis server.
# The hostname identifies a Compose service, not this container's localhost.
# db=0 selects Redis database zero.
my_redis = redis.Redis(host=redis_host, port=redis_port, db=0)


# Visiting "/" calls this function and returns the welcome message.
@app.route("/")
def welcome():
    return "Hello, World. Welcome to Flask with Redis!"


@app.route("/count")
def count():
    # Redis stores the shared counter under the key "hits".
    # INCR creates a missing counter at 1 or increments an existing one.
    # The increment is atomic: simultaneous requests cannot overwrite
    # each other's increments, including requests from different Flask containers.
    visits = my_redis.incr("hits")

    # The f-string inserts the returned count into the browser response.
    return f"This page has been visited {visits} times."


# Listen on all container interfaces so NGINX can reach Flask.
# 5000 is the internal Flask port; Compose publishes NGINX on Mac port 5002.
# This development server is used for the local learning exercise.
app.run(host='0.0.0.0', port=5000)