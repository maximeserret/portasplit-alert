import json
import os
import time
from datetime import datetime, timedelta

from telegram import send_message
from config import PRODUCTS
from stores import search_all

STATE_FILE = "state.json"
COOLDOWN_HOURS = 24


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def is_allowed_to_notify(state, key):
    if key not in state:
        return True

    last_seen = datetime.fromisoformat(state[key])
    return datetime.utcnow() - last_seen > timedelta(hours=COOLDOWN_HOURS)


def main():
    state = load_state()

    print("🔎 Début du scan produits...")

    for product in PRODUCTS:
        print(f"➡️ Recherche : {product['name']}")

        result = search_all(product["name"])

        if not result:
            print("❌ Aucun stock détecté")
            continue

        print(f"✅ Résultat trouvé: {result}")

        key = result["url"]

        if result["price"] > product["max_price"]:
            print(f"💸 Prix trop élevé: {result['price']}€")
            continue

        if not is_allowed_to_notify(state, key):
            print("⏳ Déjà notifié récemment (cooldown)")
            continue

        message = f"""
🔥 <b>Produit disponible !</b>

📦 {result['name']}
🏪 {result['store']}
💶 {result['price']} €
🔗 {result['url']}
"""

        send_message(message)

        state[key] = datetime.utcnow().isoformat()

        print("📨 Notification envoyée")

    save_state(state)
    print("✔️ Scan terminé")


if __name__ == "__main__":
    main()
