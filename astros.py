import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()
# print(json)

print("The people currently in the space are:")

for astro in json["people"]:
    print(astro["name"])
