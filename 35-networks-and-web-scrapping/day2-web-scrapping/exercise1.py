# exercise 1
# make a request to https://httpbin.org/encoding/utf8
# print it's content legible

import requests

res = requests.get("https://httpbin.org/encoding/utf8")

print(res.text)
