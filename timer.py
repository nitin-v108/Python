from time import time


def timer():
    def wrapper(func):
        start_time = time()
        print(f"Execution start time : {start_time}")
        func()
        end_time = time()
        print(f"Execution end time : {end_time}")
        print("Execution time in seconds :", end_time - start_time)
    return wrapper

@timer()
def sample_function():
    total = 0
    for i in range(1, 100000000):
        total += i
    print("Sum:", total)