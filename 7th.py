import random
import time

def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print ("Total execution time is: "+ str((end-start)*1000) + " milliseconds")
        return result
    return wrapper

@record_time
def random_num():
    numbers = range(10)
    random.shuffle(numbers)
    print numbers
    begin = time.time()
    time.sleep(random.random())
    finish = time.time()
    print ("Total sleep time is: " + str((finish - begin) * 1000) + " milliseconds")
    return numbers

if __name__ == '__main__':
    random_num()
