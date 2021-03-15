import clothes
import codecs
import json
from pprint import pprint

count1 = 0
count2 = 0
print("1 - txt file\n2 - cvs file\n3 - json file")
x = int(input("Enter func: "))
goods = []
if x == 1:
    f = open('list.txt', 'r', encoding='utf-8')
    list_prod = f.readlines()
    for i in list_prod:
        goods.append(clothes.Clothes(i.split()[0], i.split()[1], i.split()[2]))
elif x == 2:
    f = open('list.csv', 'r')
    list_prod = f.readlines()
    for i in list_prod:
        goods.append(clothes.Clothes(i.split(';')[0], i.split(';')[1], i.split(';')[2]))
elif x == 3:
    with open('list.json') as f:
        data = list(json.load(f).items())
    for i in data:
        goods.append(clothes.Clothes(i[1][0], i[1][1], i[1][2]))

for i in goods:
    if i.is_couple():
        count2 += 1
    else:
        count1 += 1
    i.show()
print("Number of goods counted as pieces:", count1)
print("Number of items counted in pairs:", count2)
