"""
SCENARIO 1:
Prepare Dish with 3 items (Bhindi, Roti & Paneer Tikka) by 1 cook at a time
Cook 1: Cooking `Bhindi` in 5 min
Cook 1: Cooking `Roti` in 5 min
Cook 1: Cooking `Paneer Tikka` in 5 min
-------------------------------------
-- Total 3 item coocked in 15 mins --
-------------------------------------

Let's understand this issue programatically.

import time


def singleCook(item):
    print(f"Started cooking {item} now.")
    time.sleep(5)
    print(f"Cooked {item} in 5 min.\n")


print("1 Cook has started cooking 3 items")
print("======================\n")
startTime1 = time.perf_counter()
singleCook("Bhindi")
singleCook("Roti")
singleCook("Paneer Tikka")
print("\n======================")
endTime1 = time.perf_counter()
print(f"Total time taken {endTime1-startTime1} mins")


"""

"""
SCENARIO 2:
Prepare Dish with 3 items (Bhindi, Roti & Paneer Tikka) by 3 cook at a time
Cook 1: Cooking `Bhindi` in 5 min
Cook 2: Cooking `Roti` in 5 min
Cook 3: Cooking `Paneer Tikka` in 5 min
-------------------------------------
-- Total 3 item coocked in 5 mins. --
-------------------------------------

Let's solve this issue programatically.
"""

import threading
import time


def allCook(item):
    print(f"Started cooking {item} now.")
    time.sleep(5)
    print(f"Cooked {item} in 5 min.\n")


t1 = threading.Thread(target=allCook, args=["Bhindi"])
t2 = threading.Thread(target=allCook, args=["Roti"])
t3 = threading.Thread(target=allCook, args=["Paneer Tikka"])

print("3 Cook has started cooking 1 item")
print("======================\n")
startTime2 = time.perf_counter()
t1.start()
t2.start()
t3.start()
print("\n==========================================")
print("PLEASE WAIT UNTIL OUR COOKS FINISH COOKING")
print("===========================================\n")
t1.join()
t2.join()
t3.join()

endTime2 = time.perf_counter()
print(f"Total time taken {endTime2-startTime2} mins")
