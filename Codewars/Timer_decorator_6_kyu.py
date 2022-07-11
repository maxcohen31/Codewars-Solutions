from time import time
def timer(limit):
    def original_func(func):
        def wrapper(*args):
            test_time = time()
            function = func(*args)
            running_time = time() - test_time 
            if running_time < limit:
                return True
            else:
                return False
        return wrapper
    return original_func

@timer(1)
def run():
    time.sleep(2)
