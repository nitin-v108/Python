def repeat(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat(5)
def who_am_i(name):
    print(f"I am {name}")

who_am_i("Nitin")