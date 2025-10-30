from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/index")
def index():
    html = f"""
    <!DOCTYPE html>
    <html>
      <body>
        <h2>NGINX Cache Test</h2>
        <p>요청 시간간: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
      </body>
    </html>
    """
    return Response(html, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
