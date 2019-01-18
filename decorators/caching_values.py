from decorators import call_counter, cache, timer


# Decorators can provide a nice mechanism for caching and memoization
# Run program with and without cache, you will see the number of calls made to the fibonacci
# function with cache it stores the intermediate calculations in stateful cache dictionary.
@cache
@call_counter
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


fibonacci(10)
fibonacci(10)

# With cache number of calls = 11
# Without cache number of calls = 354
