
from collections import Counter
PRICES = {'A':50, 'B':30, 'C':20, 'D':15}
OFFERED_QUANTITY = {'A':3, 'B':2}
OFFERED_PRICES = {'A':130, 'B':45}


def get_price(item, offercount, nooffercount):
    return nooffercount*PRICES[item] + offercount*OFFERED_PRICES[item]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #check for invalid sku
    for sku in skus:
        if sku not in PRICES:
            return -1

    total_price = 0
    itemcount = Counter()

    for item in skus:
        if item in PRICES:
            itemcount[item] += 1
        else:
            return -1
    for item in itemcount.keys():
        offercount = itemcount//OFFERED_QUANTITY[item]
        nooffercount = itemcount%OFFERED_QUANTITY[item]
        sameitems_price = get_price(item, offercount, nooffercount)
        total_price += sameitems_price

    return total_price



