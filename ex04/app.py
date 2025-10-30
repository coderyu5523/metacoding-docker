from flask import Flask
import redis
import socket

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = r.incr('count')
    hostname = socket.gethostname()
    return f"[{hostname}] 방문 횟수: {count}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
