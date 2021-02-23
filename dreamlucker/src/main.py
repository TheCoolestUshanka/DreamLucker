import math
import io 
import random

# Лого
print("-------------------\n" +
      "    DreamLucker   \n" +
      "-------------------\n")
# Запрос на значения
times = int(input("Times:"))
items = int(input("Items (not name):"))
# Генератор айди
random.seed(version=2)
for i in range(0,times):
    ritem = random.randint(0,items)
    if ritem==0:
        ritem=ritem+1
    print("id:" + str(ritem))
