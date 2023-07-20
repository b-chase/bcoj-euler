import euler_math as em
from time import perf_counter_ns

def bench_ns(func, times: int, *args, **kwargs):
    res = None
    times_ns = []
    for _ in range(times):
        start_time = perf_counter_ns()
        res = func(*args, **kwargs)
        end_time = perf_counter_ns()
        elapsed_ns = end_time - start_time
        times_ns.append(elapsed_ns)
        
    func_args = list(str(x) for x in args)
    if kwargs:
        func_args += [f"{k}={v}" for k, v in kwargs.items()]
        
    print(f"Benchmarking: {func.__name__}({','.join(func_args)})")
    for i, t_ns in enumerate(times_ns[1:min(5, times)]):
        print(f"{i+1}) {((t_ns/1000) / 1000):.5f} ms")
    
    print(f"Average time: {sum(times_ns)/len(times_ns) / 1000_000:.5f} ms")
    return res


def get_digits_mod(n:int) -> list[int]:
    d = [n%10]
    m = n//10
    while m:
        d.append(m%10)
        m//=10
    d.reverse()
    return d

def comp_bench(func_list: list, times: int, *args, **kwargs):
    for f in func_list:
        print(f"Testing function '{f.__name__}':")
        bench_ns(f, int(times), *args, **kwargs)
        print()

import math  # noqa: E402

f1 = lambda z: math.factorial(z)
f1.__name__ = 'math.factorial'
f2 = lambda z: em.factorial(z)
f2.__name__ = 'rust.factorial'

comp_bench([f1, f2], 20, 10000)
