from data import *
from operator import itemgetter

def count_distance(user_location,canteens_location):
   # user_location = pygame.mouse.get_pos()
    distance = (((user_location[0] - canteens_location[0]) ** 2) + ((user_location[1] - canteens_location[1]) ** 2)) ** 0.5
    return round((distance))

def searchbyprice(min, max):
    list1 = []
    for cant in Canteen:
        for key0, key1 in cant['itemlist']:
            if min <= cant['itemlist'][key0, key1] <= max:
                list = []
                list.append(cant["name"])
                list.append(key1)
                list.append(cant['itemlist'][key0, key1])
                list.append(cant['location'])
                list.append(key0)
                list1.append(list)
    listsorted = sorted(list1, key=itemgetter(2))
    return listsorted

def sortbybevorfood(list, bevorfood):
    listsorted = []
    for item in list:
        if item[4]== bevorfood:
            sortedlist = []
            sortedlist.append(item[0])
            sortedlist.append(item[1])
            sortedlist.append(item[2])
            sortedlist.append(item[3])
            sortedlist.append(item[4])

            listsorted.append(sortedlist)
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
                         sortedlist.append(item[0])
                         sortedlist.append(item[1])
                         sortedlist.append(item[2])
                         sortedlist.append(item[3])
                         sortedlist.append(item[4])
                         sortedlist.append(distance)
                         listsorted.append(sortedlist)

    sorted1list = sorted(listsorted ,key = itemgetter(5))

    return (sorted1list)

def sentence(list):
    for item in list:
        print("Location :", item[0], " Distance: ", item[5], "item :", item[1], "Price :", item[2])






def sortbyprice_bevfood_distance(Price,BevFood):
    if Price == [1,0,0] and BevFood == [1,0]:
        listOne = searchbyprice(0, 4.9)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)

    elif Price == [0,1,0] and BevFood == [1,0]:
        listOne = searchbyprice(5, 10)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [0,0,1] and BevFood == [1,0]:
        listOne = searchbyprice(10.1, 100)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [1,1,0] and BevFood == [1,0]:
        listOne = searchbyprice(0, 10)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [0,1,1] and BevFood == [1,0]:
        listOne = searchbyprice(5, 100)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [1,0,1] and BevFood == [1,0]:
        listOne = searchbyprice(0, 4.9)
        listTwo = searchbyprice(10.1,100)
        listCombine = listOne + listTwo
        listFour = sortbybevorfood(listCombine, "Food")
        listFive = afterpricedistance(listFour, (0, 0))
        sentence(listFive)
    elif Price == [1,1,1] and BevFood == [1,0]:
        listOne = searchbyprice(0, 100)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [1,0,0] and BevFood == [0,1]:
        listOne = searchbyprice(0, 4.9)
        listTwo = sortbybevorfood(listOne, "Beverage")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [0,1,0] and BevFood == [0,1]:
        listOne = searchbyprice(5, 10)
        listTwo = sortbybevorfood(listOne, "Beverage")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [0,0,1] and BevFood == [0,1]:
        listOne = searchbyprice(5, 10)
        listTwo = sortbybevorfood(listOne, "Beverage")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [1,1,0] and BevFood == [0,1]:
        listOne = searchbyprice(0, 10)
        listTwo = sortbybevorfood(listOne, "Beverage")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [0,1,1] and BevFood == [0,1]:
        listOne = searchbyprice(5, 100)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [1,0,1] and BevFood == [0,1]:
        listOne = searchbyprice(0, 4.9)
        listTwo = searchbyprice(10.1,100)
        listCombine = listOne + listTwo
        listFour = sortbybevorfood(listCombine, "Beverage")
        listFive = afterpricedistance(listFour, (0, 0))
        sentence(listFive)
    elif Price == [1,1,1] and BevFood == [0,1]:
        listOne = searchbyprice(0, 100)
        listTwo = sortbybevorfood(listOne, "Food")
        listThree = afterpricedistance(listTwo, (0, 0))
        sentence(listThree)
    elif Price == [1,0,0] and BevFood == [1,1]:
        listOne = searchbyprice(0, 4.9)

        listThree = afterpricedistance(listOne, (0, 0))
        sentence(listThree)
    elif Price == [0,1,0] and BevFood == [1, 1]:
        listOne = searchbyprice(5, 10)

        listThree = afterpricedistance(listOne, (0, 0))
        sentence(listThree)
    elif Price == [0,0,1] and BevFood == [1, 1]:
        listOne = searchbyprice(10.1, 100)

        listThree = afterpricedistance(listOne, (0, 0))
        sentence(listThree)
    elif Price == [1, 1, 0] and BevFood == [1, 1]:
        listOne = searchbyprice(0, 10)

        listThree = afterpricedistance(listOne, (0, 0))
        sentence(listThree)
    elif Price == [0, 1, 1] and BevFood == [1, 1]:
        listOne = searchbyprice(10, 100)

        listThree = afterpricedistance(listOne, (0, 0))
        sentence(listThree)
    elif Price == [1,0,1] and BevFood == [1,1]:
        listOne = searchbyprice(0, 4.9)
        listTwo = searchbyprice(10.1,100)
        listCombine = listOne + listTwo

        listFive = afterpricedistance(listCombine, (0, 0))
        sentence(listFive)
    else:
        listOne = searchbyprice(0, 100)

        listThree = afterpricedistance(listOne, (0, 0))
        sentence(listThree)

def searchbyfoodname (name):
    dict_name = ['FoodCourt1', 'FoodCourt2', 'FoodCourt9', 'FoodCourt11', 'FoodCourt13', 'FoodCourt14', 'FoodCourt16',
                 'Anandakitchen', 'FoodgleFoodCourt', 'NorthHillFoodCourt']
    set = 0
    for cant in Canteen:
        for key0,key1 in cant['itemlist']:
            if name in key1:
                print ("Food :",key1,"Price :", cant['itemlist'][key0,key1],"Location :",dict_name[set])
        set += 1

if __name__ == '__main__':
    # test = count_distance((0,0),(4,4))
    # test = searchbyprice(5.0, 7.0)
    test = sortbyprice_bevfood_distance([1,0,1],[1,1])
    print(test)


