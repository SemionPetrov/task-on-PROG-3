import time
from time import perf_counter

class Timer:
    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Время выполнения: {self.elapsed_time:.4f} секунд")

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def calculate_fibonacci(n):
    with Timer() as timer:
        fib_gen = fibonacci_generator(n)
        for _ in fib_gen:
            pass
    return timer.get_elapsed_time()

if __name__ == "__main__":
    n_fibonacci = 1000000
    elapsed = calculate_fibonacci(n_fibonacci)