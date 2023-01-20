import requests
from flask import Flask
import time
from requests.exceptions import HTTPError
from retry import retry

app = Flask(__name__)

# def retry(func, retries=1000):
#     def retry_wrapper(*args, **kwargs):
#         attempts = 0
#         while attempts < retries:
#             try:
#                 return func(*args, **kwargs)
#             except HTTPError as e:
#                 if e.code == 500:
#                     time.sleep(2)
#                     attemps += 1
#     return retry_wrapper

@retry(HTTPError,tries=10, delay=2)
def contact_service(url):
    return requests.get(url)
    

@app.route("/")
def index():
    try:
        r = contact_service('http://api2')
        text = r.text
        return text
    except HTTPError as e:
        if e.code == 500:
            return "Servirce currently unavailable. Waiting..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)