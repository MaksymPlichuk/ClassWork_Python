#---------------------------------- decorators
def my_decorator(func):
    def private_decorator():
        print("--My decorator--")
        func()
        print("--End decorator--")
    return private_decorator

@my_decorator
def hello_message():
    print("sasdfsdfsdfsdf")

hello_message()
#---------------------------------- Closures

def view_msg(msg):
    message = msg[0:9]
    # print(message)
    def private_func():
        print(message)
    return private_func

ptr = view_msg("applebanana")
ptr()
#---------------------------------- yield

def getnums():
    return [1,2,3]

print(f"def numbers: {getnums()}")

def get_yield_num():
    yield 1
    yield 2
    yield 7

for item in get_yield_num():
    print(item, end="\t")

def yield_counter(n):
    i=0;
    while i<=n:
        yield i
        i +=2

for item in yield_counter(8):
    print(item, end="\t")
