import time

def timer(fn):
    def check_time(*args, **kwargs):
        start_time = time.time()
        res = fn()
        time.sleep(1)
        print('Function spent: ' , start_time - time.time())
    return check_time


@timer
def my_range(n=0):
    for i in range(n):
        print(i, end=" ")

print(my_range(600000))