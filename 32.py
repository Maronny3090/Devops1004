import requests
from werkzeug.http import http_date

response = requests.post("http://127.0.0.1:5001/whatismyname")
print(response.txt)
expected = "saved new car"
assert  expected == response.txt