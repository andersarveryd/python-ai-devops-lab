import requests

print("Hello Anders, Python funkar! 🚀")

r = requests.get("https://api.github.com")
print("GitHub API status:", r.status_code)
