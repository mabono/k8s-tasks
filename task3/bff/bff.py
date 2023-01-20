import requests
from flask import Flask


app = Flask(__name__)

@app.route("/api1")
def index():
    # text = contact_service('google.com')
    r = requests.get('http://api1')
    return r.text


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)