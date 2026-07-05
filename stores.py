import requests

def search_all(product_name: str):
    url = f"https://www.darty.com/nav/recherche/{product_name.replace(' ', '+')}"

    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    print("STATUS:", r.status_code)
    print("LENGTH:", len(r.text))

    return None
