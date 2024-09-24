# Does not work - probably because of zscaler
import requests
import json

def fetch_nobel_prizes(url, prams=None):
    response = requests.get(url, params=prams)
    response.raise_for_status()
    return response.json()

def download_complete_dataset():
    base_url = "https://api.nobelprize.org/2.1/laureates"
    all_nobel_laureates = []
    offset = 0
    limit = 25

    while True:
        params = {"offset": offset, "limit": limit}
        data = fetch_nobel_prizes(base_url, params)
        all_nobel_laureates.extend(data["laureates"])

        # Check if there is a next page
        if "next" not in data["links"]:
            break
        offset += limit

    with open("data/laureates.json", "w") as file:
        json.dump(all_nobel_laureates, file, indent=4)

if __name__ == "__main__":
    download_complete_dataset()