from flask import Flask

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return "favicon"

@app.route("/")
def index():
    str = """
        <html>
            <head>
                <title>GitPod Test</title>
            </head>
            <body>
                <h1>Hello GitPod
            </body>
        </html>
    """
    return str

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)