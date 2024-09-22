from functools import wraps
import time

def timer(function):
    @wraps(function)
    def count_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = function(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"The function {function.__name__} took {total_time:4f} seconds")
        return result
    return count_timer