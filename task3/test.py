import requests
from flask import Flask
import time
from requests.exceptions import HTTPError, RequestException
# from retry import retry

app = Flask(__name__)

def retry(func, retries=3):
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except RequestException as e:
                print(e)
                time.sleep(2)
                attempts += 1
    return retry_wrapper

@retry
def contact_service(url):
    r = requests.get(url)
    return r.text
    

@app.route("/")
def index():
    # r = contact_service('http://ass')
    # try:
    #     r.raise_for_status()
    # except:
    #         return "Servirce currently unavailable. Waiting..."
    # else:
    #     text = r.text
    #     return text
    text = contact_service("http://10.1.0.239:80")
    print(text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)