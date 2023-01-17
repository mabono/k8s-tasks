from flask import Flask

app = Flask(__name__)

@app.route('/api2')
def hello():
    return "api2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)