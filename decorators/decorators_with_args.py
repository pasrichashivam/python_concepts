from decorators import repeat

# To call the funtion for a number of times
@repeat(num_times=4)
def greet(name):
    print("Hello {0}".format(name))

greet("Shivam")