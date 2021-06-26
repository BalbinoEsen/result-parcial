import requests

""" response = requests.get("http://localhost:23512/city/1")
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson) """

""" response = requests.post("http://localhost:23512/city/645")
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson) """

""" data = {
    "Name": "city01",
    "CountryCode": "AFG",
    "District": "district01",
    "Population": 18,
}
response = requests.put("http://localhost:23512/city/0", data=data)
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson) """

""" data = {
    "Name": "city01x",
    "CountryCode": "AFG",
    "District": "district01x",
    "Population": 20,
}
response = requests.patch("http://localhost:23512/city/4083", data=data)
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson) """

""" response = requests.delete("http://localhost:23512/city/4083")
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson) """
