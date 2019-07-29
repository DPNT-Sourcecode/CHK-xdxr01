
from collections import defaultdict
product_list = ['A', 'B', 'C', 'D']
product_price = {'A':50, 'B':30, 'C':20, 'D':15}
offered_quantity = {'A':3, 'B':2}
offered_price = {'A':130, 'B':45}

def get_price(item, offercount, nooffercount):
    return nooffercount*product_price[item] + offercount*offered_price[item]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_price = 0
    itemcount = defaultdict(int)
    for item in skus:
        if item in product_list:
            itemcount[item] += 1
        else:
            return -1
    for item in itemcount.keys():
        offercount = itemcount//offered_quantity[item]
        nooffercount = itemcount%offered_quantity[item]
        sameitems_price = get_price(item, offercount, nooffercount)
        total_price += sameitems_price

    return total_price




