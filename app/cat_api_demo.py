import requests

def fetch_random_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()  # kolla om requesten lyckades
        data = response.json()
        print("Här är en kattbild-URL:", data[0]["url"])
    except requests.exceptions.RequestException as e:
        print("Något gick fel:", e)

if __name__ == "__main__":
    fetch_random_cat()
