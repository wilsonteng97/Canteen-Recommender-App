from tkinter import *
from operator import itemgetter
from pprint import pprint

from data import *

def count_distance(user_location,canteens_location):
    dist = math.sqrt((canteens_location[1] - user_location[0]) ** 2 + (canteens_location[1] - user_location[0]) ** 2)
    roundeddist = round(dist)
    return roundeddist


def searchbyprice(min, max=99999):
    list1 = []
    for cant in Canteen:
        for key0, key1 in cant['itemlist']:
            if min <= cant['itemlist'][key0, key1] <= max:

                list1.append((cant["name"],key1,cant['itemlist'][key0, key1],cant['location'],key0))

    listsorted = sorted(list1, key=itemgetter(2))
    return listsorted


def sortbybevorfood(list,bevorfood):
    listsorted = []
    for item in list:

        if item[4]== bevorfood:

            listsorted.append((item[0], item[1], item[2], item[3], item[4]))

    return listsorted





def afterpricedistance(list,location):
    listsorted =[]
    for item in list:
        for cant in Canteen:
            for foodbev,foodname in cant["itemlist"]:

                if cant["name"]==item[0] and foodname==item[1]:

                     distance = count_distance(location,item[3])
                     sortedlist = []
                     if distance <=500:

                         listsorted.append((item[0],item[1],item[2],item[3],item[4],distance))

    sorted1list = sorted(listsorted ,key = itemgetter(5))

    return (sorted1list)

def sentence(list):
    for item in list:
        print("Location :", item[0], " Distance: ", item[5], "item :", item[1], "Price :", item[2])






def sortbyprice_bevfood_distance(Price,BevFood):
    mainlist = []
    mainlist1 = []
    mainlist2 = []
    list3 = []

    if Price[0] == 1:
        mainlist.append(searchbyprice(0,4.9))
    else:
        pass

    if Price[1] == 1:

        mainlist.append(searchbyprice(5, 10))
    else:
        pass

    if Price[2] == 1:

        mainlist.append(searchbyprice(10.1))
    else:
        pass
    for item in mainlist:
        for i in item:
          mainlist1.append(i)



    if  BevFood[0] == 1:
        mainlist2.append(sortbybevorfood(mainlist1, "Food"))
    if BevFood[1] == 1:
            mainlist2.append(sortbybevorfood(mainlist1, "Beverage"))


    for item in mainlist2:
        for i in item:
            list3.append(i)
    return list3   

def unsortedlist(bevfood):
    for cant in Canteen:
        unsortedlist = []
        for itemtype, item in cant["itemlist"]:
            if bevfood[0] == 1:
                if itemtype == "Food":
                    price = cant["itemlist"][(itemtype, item)]
                    entry = [item, price]
                    unsortedlist.append(entry)

            if bevfood[1] == 1:
                if itemtype == "Beverage":
                    price = cant["itemlist"][(itemtype, item)]
                    entry = [item, price]
                    unsortedlist.append(entry)       
    return unsortedlist
    

def sortby_price_bevfood(pricerange, bevfood):
    collatedsortedlist = []
    for cant in Canteen:
        unsortedlist = []
        for itemtype, item in cant["itemlist"]:
            if bevfood[0] == 1:
                if itemtype == "Food":
                    price = cant["itemlist"][(itemtype, item)]
                    entry = [item, price]
                    unsortedlist.append(entry)

            if bevfood[1] == 1:
                if itemtype == "Beverage":
                    price = cant["itemlist"][(itemtype, item)]
                    entry = [item, price]
                    unsortedlist.append(entry)
            unsortedlist = unsortedlist()
            sortedlist = [cant["name"], sorted(unsortedlist, key=lambda entry: entry[1])] 
        collatedsortedlist.append(sortedlist)
    return collatedsortedlist

def return_selected_foodcourt(selection_tuple=(3,)):
    pass

        
            

if __name__ == '__main__':
    # test = count_distance((0,0),(4,4))
    # test = searchbyprice(5.0, 7.0)
    # test = sortbyprice_bevfood_distance([1,0,0],[1,1])
    # test = sortby_price_bevfood([1,0,0],[1,1])
    # pprint(test)
    print(unsortedlist([0,1]))


