import timeit
import matplotlib.pyplot as plt
import numpy as np


def function(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1


def run_benchmark(input_size):
    setup_code = f"from __main__ import function; input_value = {input_size}"
    stmt = "function(input_value)"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=5)
    return execution_time


def create_plot(results):
    sizes, times = zip(*results)    # zip needed b/c of too many values to unpack warning
    plt.plot(sizes, times, marker='o', linestyle='-', color='b')

    degree = 2
    coefficients = np.polyfit(sizes, times, degree)

    estimated_curve = np.poly1d(coefficients)

    upper_bound = 2 * np.poly1d(coefficients)
    lower_bound = 1/2 * np.poly1d(coefficients)

    # Plotting
    plt.plot(sizes, times, marker='o', linestyle='-', color='b', label='Actual Runtime')
    plt.plot(sizes, estimated_curve(sizes), linestyle='--', color='black', label='Estimated Curve')
    plt.plot(sizes, upper_bound(sizes), linestyle='--', color='red', label='Upper bound 2(n^2+1)')
    plt.plot(sizes, lower_bound(sizes), linestyle='--', color='green', label='Lower bound (1/2)(n^2+1)')


    # Add a vertical line or marker for n0
    plt.axvline(x=1, color='r', linestyle='--', label=f'Approx. n0 at x=1')

    plt.xlabel('n value')
    plt.ylabel('Runtime (seconds)')
    plt.title('Function Benchmark')
    plt.legend()
    plt.grid(True)
    plt.show()


# runs the benchmark portion
input_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
time_results = []

print("\nBenchmark Testing:")

for size in input_sizes:
    time = run_benchmark(size)
    time_results.append((size, time))
    print(f"Input Size: {size}, Execution Time: {time:.6f} seconds")

create_plot(time_results)