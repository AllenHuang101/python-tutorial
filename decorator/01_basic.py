
def welcome(fn):
    def wrapper(*args, **kwargs):
        print("Welcome")
        result = fn(*args, **kwargs)
        return result
    
    return wrapper

def welcome_with_args(name):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print(f"Welcome {name}")
            result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorator

def my_fun(message: str):
    # print("Welcome")
    print(f"Hello {message}")

@welcome
def my_fun2(message: str):
    # print("Welcome")
    print(f"Hello2 {message}")
    
f1 = welcome(my_fun)
f1("Allen")

# f2 = welcome(my_fun2)
# f2("Bob")
my_fun2("Bob")

@welcome_with_args("Jack")
def my_fun3(message: str):
    print(f"Hello3 {message}")
    
my_fun3("Jack")