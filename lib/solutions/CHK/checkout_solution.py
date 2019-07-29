
from collections import Counter
from operator import itemgetter

INVENTORY = {
    'A': {'price': 50, 'offer': [{'cnt': 3, 'price': 130}, {'cnt': 5, 'price': 200}]},
    'B': {'price': 30, 'offer': [{'cnt': 2, 'price': 45}], 'free': {'sku': 'E', 'cnt': 2}},
    'C': {'price': 20},
    'D': {'price': 15},
    'E': {'price': 40},
    'F': {'price': 10, 'free': {'sku': 'F', 'cnt': 2}},
    'G': {'price': 20},
    'H': {'price': 10, 'offer': [{'cnt': 5, 'price': 45}, {'cnt': 10, 'price': 80}]},
    'I': {'price': 35},
    'J': {'price': 60},
    'K': {'price': 80, 'offer': [{'cnt': 2, 'price': 150}]},
    'L': {'price': 90},
    'M': {'price': 15, 'free': {'sku': 'N', 'cnt': 3}},
    'N': {'price': 40},
    'O': {'price': 10},
    'P': {'price': 50, 'offer': [{'cnt': 5, 'price': 200}]},
    'Q': {'price': 30, 'offer': [{'cnt': 3, 'price': 80}], 'free': {'sku': 'R', 'cnt': 3}},
    'R': {'price': 50},
    'S': {'price': 30},
    'T': {'price': 20},
    'U': {'price': 40, 'free': {'sku': 'U', 'cnt': 3}},
    'V': {'price': 50, 'offer': [{'cnt': 2, 'price': 90}, {'cnt': 3, 'price': 130}]},
    'W': {'price': 20},
    'X': {'price': 90},
    'Y': {'price': 10},
    'Z': {'price': 50}










}

def get_free_items(sku):
    if 'free' in INVENTORY[sku]:
        return INVENTORY[sku]['free']
    else:
        return None

def get_offers(item):
    if 'offer' in INVENTORY[item]:
        return INVENTORY[item]['offer']
    else:
        return None

def get_price(item, quantity, offers):
    final_cost = 0
    if offers:
        for key in sorted(offers, key=itemgetter('cnt'), reverse = True):
            bulk_offer_count = quantity//key['cnt']
            bulk_offer_cost = bulk_offer_count * key['price']
            quantity = quantity%key['cnt']
            final_cost += bulk_offer_cost
    no_offer_cost = quantity * INVENTORY[item]['price']
    final_cost += no_offer_cost
    return final_cost

def adjust_free_skus(cart):
    final_cart = cart
    for sku in cart:
        free = get_free_items(sku)
        if free:
            other_sku = free['sku']
            other_sku_offer_cnt = free['cnt']
            if other_sku in cart:
                other_sku_cart_cnt = cart[other_sku]
                # check for quantity for free offer on same sku
                if other_sku == sku:
                    group_count = other_sku_offer_cnt+1
                    group_eligible =  other_sku_cart_cnt // group_count
                    #standalone_count = other_sku_cart_cnt % group_count
                    final_cart[sku] -= group_eligible
                else:
                    this_sku_free_cnt = other_sku_cart_cnt // other_sku_offer_cnt
                    final_cart[sku] -= this_sku_free_cnt
    return final_cart

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
        offers = get_offers(item)
        item_price = get_price(item, quantity, offers)
        total_price += item_price

    return total_price

