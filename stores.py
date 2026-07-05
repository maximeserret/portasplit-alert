import random

def search_all(product_name: str):
    """
    Simulation de stock (remplacera ensuite le vrai scraping)
    """

    if random.random() < 0.25:  # 25% chance dispo
        return {
            "name": product_name,
            "price": random.randint(850, 1100),
            "url": f"https://example.com/{product_name.replace(' ', '-').lower()}",
            "store": "DemoStore"
        }

    return None
