import time
import threading


def allCook(item):
    print(f"Started cooking {item} now.")
    time.sleep(2)  # reduced to 1s for quicker demo
    print(f"Cooked {item} in 2 sec.\n")


def main():
    t1 = threading.Thread(target=allCook, args=("Bhindi",))
    t2 = threading.Thread(target=allCook, args=("Roti",))
    t3 = threading.Thread(target=allCook, args=("Paneer Tikka",))

    t1.start()
    t2.start()
    t3.start()

    # wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()

    print("\nAll cooking done. Total time ~2 sec (concurrent)")


if __name__ == "__main__":
    main()
