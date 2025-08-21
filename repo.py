import requests

# Apna GitHub username likho
username = "AleenaZainab1"

# API URL
url = f"https://api.github.com/users/{username}/repos"

# Request bhejna
response = requests.get(url)

print("\n--- GitHub Repositories ---")
if response.status_code == 200:
    repos = response.json()
    if repos:
        for repo in repos:
            print("-", repo["name"])
    else:
        print("No repositories found!")
else:
    print("Error:", response.status_code)
