import time
from concurrent.futures import ThreadPoolExecutor


def allCook(item):
    print(f"Started cooking {item} now.")
    time.sleep(5)
    print(f"Cooked {item} in 5 min.\n")
    return f"{item} ready to serve..."


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        cook1 = executor.submit(allCook, "Bhindi")
        cook2 = executor.submit(allCook, "Roti")
        cook3 = executor.submit(allCook, "Paneer Tikka")
        print(cook1.result())
        print(cook2.result())
        print(cook3.result())


poolingDemo()
