import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def search_all(product_name: str):
    query = product_name.replace(" ", "+")
    url = f"https://www.darty.com/nav/recherche/{query}"

    r = requests.get(url, headers=HEADERS, timeout=15)

    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "lxml")

    product = soup.select_one(".product-list ul li")

    if not product:
        return None

    title = product.select_one(".product-title")
    price = product.select_one(".darty_price_display")
    link = product.select_one("a")

    if not title or not price or not link:
        return None

    try:
        price_value = float(price.text.replace("€", "").replace(",", ".").strip())
    except:
        return None

    return {
        "name": title.text.strip(),
        "price": price_value,
        "url": "https://www.darty.com" + link["href"],
        "store": "Darty"
    }
