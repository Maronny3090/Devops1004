import requests
response = requests.get("https://api.github.com/users/avielb/repos")

print(response.json())

results = response.json()

for repo in results:
    print(repo["name"])

