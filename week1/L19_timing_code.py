import time

# start = time.perf_counter()
# ans = 1
# for i in range(100000):
#     ans += i

# end = time.perf_counter()

# elapsed = end - start

# print(elapsed)

# TIMER ERROR

class TimeError(Exception):
    """A custom exception used to report errors in use of Timer class"""

# create a timer class

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None
    
    def start(self):
        """Start a new timer"""
        if self.start_time is not None:
            raise TimeError("Timer is running. Use .stop()")
        self.start_time = time.perf_counter()
    
    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self.start_time is None:
            raise TimeError("Timer is not running. Use .start()")
        self.elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
    
    def elapsed(self):
        """Report elapsed time"""
        if self.elapsed_time is None:
            raise TimeError("Timer has not been run yet. Use .start()")
        return (self.elapsed_time)
    
    def __str__(self):
        """print() prints elapsed time"""
        return (str(self.elapsed_time))

    
timer = Timer()

# timer.start()

# ans = 1
# for i in range(100000):
#     ans += i

# timer.stop()

# print(timer.elapsed())

for j in range(4,9):
    timer.start()
    n = 0
    for i in range(10**j):
        n = n + 1
    timer.stop()
    print(j,timer)