
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask DevOps Demo</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>My First DevOps Project</h1>
            <p>Flask application is running successfully!</p>
            <p>Built with Python, Flask, and Docker.</p>
            <a href="/health">Check Application Health</a>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
