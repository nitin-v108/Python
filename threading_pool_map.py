import time
from concurrent.futures import ThreadPoolExecutor


def allCook(item):
    print(f"Started cooking {item} now.")
    time.sleep(5)
    print(f"Cooked {item} in 5 min.\n")
    return f"{item} ready to serve..."


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        orderItems = ["Bhindi", "Roti", "Paneer Tikka"]
        cookedItems = executor.map(allCook, orderItems)
        for cookedItem in cookedItems:
            print(cookedItem)


poolingDemo()
