from decorators import timer, singleton, CountCalls


class TestClass:
    # Decorator can be applied to method in a class also
    @timer
    def stress_method(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(9999)])


tw = TestClass()
tw.stress_method(999)


@CountCalls
def say_whee():
    print("Whee!")


for i in range(3):
    say_whee()


@singleton
class TestOne:
    pass

first_one = TestOne()
another_one = TestOne()

print(id(first_one))
print(id(another_one))
# id of both objects will be same as they are referencing to same object
# because of singletom behaviour
