from flask import Flask
import random
from requests.exceptions import HTTPError

app = Flask(__name__)

@app.route("/")
def index():
    if_error = random.randint(0,1)
    if (if_error == 1):
        raise Exception(500)
    else:
        return "Working just fine"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)