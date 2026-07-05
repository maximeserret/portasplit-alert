import json, os
from telegram import send_message
from config import PRODUCT_KEYWORDS, MAX_PRICE
from stores import search_all

STATE_FILE = "state.json"

def load():
    if not os.path.exists(STATE_FILE):
        return {}
    return json.load(open(STATE_FILE))

def save(s):
    json.dump(s, open(STATE_FILE, "w"))

def run():
    state = load()

    for p in PRODUCT_KEYWORDS:
        r = search_all(p)
        if not r:
            continue

        if r["price"] <= MAX_PRICE and not state.get(r["url"]):
            send_message(
                f"🔥 Disponible !\n{r['name']}\n{r['price']}€\n{r['url']}"
            )
            state[r["url"]] = True

    save(state)

run()
