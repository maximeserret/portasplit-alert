import random

def search_all(keyword):
    if random.random() < 0.2:
        return {
            "name": keyword,
            "price": 899,
            "url": "https://example.com/product",
            "store": "DemoStore"
        }
    return None
