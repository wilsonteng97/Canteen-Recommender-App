from tkinter import *
from operator import itemgetter
from pprint import pprint
import math

from data import *

def count_distance(user_location, canteens_location):
    dist = math.sqrt((canteens_location[0] - user_location[0]) ** 2 + (canteens_location[1] - user_location[1]) ** 2)
    roundeddist = round(dist)
    return roundeddist

def sort_canteen_bydistance(CanteenList, UserPosition):
    return sorted(CanteenList, key=lambda x: count_distance(UserPosition, x["location"]))

def sortby_price_bevfood(CanteenList, pricerange, bevfood):
    collatedsortedlist = []
    for cant in CanteenList:
        unsortedlist = []
        for itemtype, item in cant["itemlist"]:
            if bevfood[0] == 1:
                if itemtype == "Food":
                    price = cant["itemlist"][(itemtype, item)]
                    if pricerange[0] == 1:
                        if price < 5:
                            entry = [item, price]
                            unsortedlist.append(entry)
                    if pricerange[1] == 1:
                        if 5 <= price <= 10:
                            entry = [item, price]
                            unsortedlist.append(entry)
                    if pricerange[2] == 1:
                        if price > 10:
                            entry = [item, price]
                            unsortedlist.append(entry)

            if bevfood[1] == 1:
                if itemtype == "Beverage":
                    price = cant["itemlist"][(itemtype, item)]
                    if pricerange[0] == 1:
                        if price < 5:
                            entry = [item, price]
                            unsortedlist.append(entry)
                    if pricerange[1] == 1:
                        if 5 <= price <= 10:
                            entry = [item, price]
                            unsortedlist.append(entry)
                    if pricerange[2] == 1:
                        if price > 10:
                            entry = [item, price]
                            unsortedlist.append(entry)
            sortedlist = [cant["name"], sorted(unsortedlist, key=lambda entry: entry[1])] 
        collatedsortedlist.append(sortedlist)
    return collatedsortedlist

def return_selected_foodcourt(CanteenList, selection_tuple):
    # selection = selection_tuple[0]
    return CanteenList[selection_tuple]


if __name__ == '__main__':
    test0 = sort_canteen_bydistance(Canteen, (0,0))
    test1 = sortby_price_bevfood(test0, [1,1,0], [1,0])
    test2 = return_selected_foodcourt(test1, 3)
    pprint(test0)
    print()
    pprint(test1)
    print()
    pprint(test2)
