from datetime import datetime
import time


# Demo decorator to show the flow of call stack.
def my_decorator(func):
    def wrapper():
        print("Funtionality before the function is called.")
        func()
        print("Funtionality after the function is called.")

    return wrapper


# To call the function only between the 7 AM to 10 PM
def call_using_time(func):
    def call_after_7_before_22():
        if 7 <= datetime.now().hour < 22:
            func()

    return call_after_7_before_22


# Convert arguments in integer
def cast_to_int(func):
    def wrapper_do_twice(*args, **kwargs):
        args = map(int, args)
        return func(*args, **kwargs)

    return wrapper_do_twice


# Decorating Functions With Arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


# Timer decorator prints the time took to do the functionality
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        print(str(time.time() - start) + " Seconds")
        return val

    return wrapper


# Call the function for num_times number of times
def repeat(num_times):
    def decorator_function(func):
        def wrapper(*args):
            for i in range(num_times):
                func(*args)

        return wrapper

    return decorator_function


# Counter Stateful Decorators
def call_counter(func):
    def helper(*args):
        helper.calls += 1
        print(helper.calls)
        return func(*args)

    helper.calls = 0
    return helper


# Caching / Memoization
def cache(func):
    def wrapper(*args):
        cache_key = args
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args)
        return wrapper.cache[cache_key]

    wrapper.cache = {}
    return wrapper


# Creating Singletons
# @singleton decorator turns a class into a singleton by storing the first instance
# of the class as an attribute. Later attempts at creating an instance simply return the
# stored instance cls is the constructor function, it will construct class and call
# the __init__(self) function.
def singleton(cls):
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


# The .__call__() method is executed each time you try to call an instance of the class:
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print("Call {0}".format(self.num_calls))
        return self.func(*args, **kwargs)
