from flask import Flask
from urllib.request import urlopen
from urllib.error import HTTPError
from retrying import retry

app = Flask(__name__)

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=3)
def contact_service(url):
    return urlopen(url).read()
    

@app.route("/")
def index():
    try:
        return contact_service("http://api2")
    except HTTPError as error:
        if error.code == 500:
            return "Service temporary unavailable. Please refresh..."
        else:
            raise error

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)