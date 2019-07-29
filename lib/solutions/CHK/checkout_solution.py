
from collections import Counter

INVENTORY = {
    'A': {'price': 50, 'offer': [{'cnt': 3, 'price': 130}, {'cnt': 5, 'price': 200}]},
    'B': {'price': 30, 'offer': {'cnt': 2, 'price': 45}},
    'C': {'price': 20},
    'D': {'price': 15},
    'E': {'price': 40, 'free': [{'cnt':2, 'sku': 'A'}]}
}

def get_free_items(sku):
    if 'free' in INVENTORY[sku]:
        return INVENTORY[sku]['free']
    else:
        return None

def get_offer(item):
    if 'offer' in INVENTORY[item]:
        return INVENTORY[item]['offer']
    else:
        return None

def get_price(item, quantity, offer):
    final_cost = 0
    if offer:
        bulk_offer_count = quantity//offer['cnt']
        bulk_offer_cost = bulk_offer_count * offer['price']
        quantity = quantity%offer['cnt']
        final_cost += bulk_offer_cost
    no_offer_cost = quantity * INVENTORY[item]['price']
    final_cost += no_offer_cost
    return final_cost

def adjust_free_skus(cart):
    for sku in cart:
        sku_quantity = sku['cnt']
        total_free = 0
        free = get_free_items(sku)
        for f in free:
            free_cnt = sku_quantity//f['cnt']
            total_free += free_cnt

def checkout(skus):
    #check for invalid sku
    for sku in skus:
        if sku not in INVENTORY:
            return -1

    total_price = 0
    cart = Counter(skus)
    cart = adjust_free_skus(cart)

    for item in cart:
        quantity = cart[item]
        offer = get_offer(item)
        item_price = get_price(item, quantity, offer)
        total_price += item_price

    return total_price

