def decorators(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorators
def start_job():
    print("Processing")

start_job()
