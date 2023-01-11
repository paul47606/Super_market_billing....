from datetime import datetime

name = input("Welcome! to Paul's supermarket\nplease enter your name: ")
mobile = input("Enter your Mobile number: ")

# list of items
list = '''

    rice    Rs 20/Kg
    sugar   Rs 30/Kg
    salt    Rs 20/Kg
    oil     Rs 80/Kg
    panner  Rs 110/Kg
    maggi   Rs 50/Kg
    boost   Rs 90/Each
    '''
# declearition
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

# rates for items (dic)

items = {'rice': 20,
         'sugar': 30,
         'salt': 20,
         'oil': 80,
         'panner': 110,
         'maggi': 50,
         'boost': 90,
         }

# conditions

option = int(input("Press '1' for List of items: "))

if option == 1:
    print(list)

for i in range(len(items)):
    inp1 = int(input("For buying press 1 or For exist press 2: "))
    if inp1 == 2:
        break

    if inp1 == 1:
        item = input("Enter your item: ")
        quantity = int(input("Enter your Quantity(Kg): "))
        if item in items.keys():
            price = quantity * (items[item]) # price of product with kgs mulitiplication
            pricelist.append((item,quantity,items,price))
            totalprice = totalprice + price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*18)/100
            final_amount = gst + totalprice
        else:
            print("sorry... you entered item not is present")

    else:
        print("you entered wrong number")

    inp = input(" 1. Bill generate press yes \n 2. without bill press no: ")
    if inp == 'yes':
        pass
        if final_amount!=0:
            for i in range(len(pricelist)):
                print(i, ilist[i], qlist[i], plist[i])


print(final_amount)
