from time import sleep
from threading import *

# Started execusion by main thread..... [T1]


class Sabji(Thread):
    def run(self):
        sabjiOrders = ["Bhindi", "Batata", "Paneer Tikka"]
        for sabji in sabjiOrders:
            print(f" [Sabji] Started cooking {sabji}")
            sleep(2)


class Roti(Thread):
    def run(self):
        rotiOrder = ["Chapati", "Naan", "Paratha"]
        for roti in rotiOrder:
            print(f" [Roti] Started cooking {roti}")
            sleep(2)


# running main thread.................. [T1]

sabji = Sabji()
roti = Roti()

print("[Waiter] Gathering Order")

# Created 'sabji' new thread........... [T2]
sabji.start()

# Added sleep to solve collision between both thread
sleep(0.2)

# Created 'roti' new thread............ [T3]
roti.start()


# Only need to add below line whenever we want to stop further execusion until 'sabji' & 'roti' process completed, then need to add below code.
sabji.join()
roti.join()

# Ended 'sabji' thread................. [T2]
# Ended 'roti' thread.................. [T3]

# running main thread.................. [T1]
print("[Cook] Hey, all ordered items ready to serve.")
