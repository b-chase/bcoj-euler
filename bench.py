import euler_math as em
from time import perf_counter_ns

def bench_ns(func, iter: int, *args, **kwargs):
    res = None
    times_ns = []
    for _ in range(iter):
        start_time = perf_counter_ns()
        res = func(*args, **kwargs)
        end_time = perf_counter_ns()
        elapsed_ns = end_time - start_time
        times_ns.append(elapsed_ns)

    print(f"Benchmarking: {func.__name__}({args}, {kwargs})")
    for i, t_ns in enumerate(times_ns):
        print(f"{i+1}) {((t_ns/1000) / 1000):.5f} ms")
    
    print(f"Average time: {sum(times_ns)/len(times_ns) / 1000_000:.5f} ms")
    return res


b = bench_ns(em.divisors_of_n, 1, 876543219)
print(b)