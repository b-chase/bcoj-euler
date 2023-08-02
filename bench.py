import euler_math as em
from euler_tools.math import get_digits
from time import perf_counter_ns
import math  # noqa: E402

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

def est_runtime(func_of_n, range_n, rep_times=5):
    avg_times = []
    for n in range_n:
        times_ns = []
        for _ in range(rep_times):
            start_time = perf_counter_ns()
            _res = func_of_n(n)
            end_time = perf_counter_ns()
            elapsed_ns = end_time - start_time
            times_ns.append(elapsed_ns)
        avg_t = sum(times_ns)/len(times_ns)
        avg_times.append(avg_t)
        print(f"fn({n}) completed on average in {avg_t/1e6:.5f} ms")
    comp_funcs = {
        'LogN': (lambda x: math.log(x)), 
        'N': (lambda x: x), 
        'NlogN': (lambda x: x*math.log(x)), 
        'N^1.5': (lambda x: x**1.5),
        'N2': (lambda x: x**2)
    }
    
    rel_times = [t / avg_times[0] for t in avg_times]
    print("Time Ratios for actual function:", ', '.join([f"{x:.3f}" for x in rel_times]))
    for cfn in ['LogN', 'N', 'NlogN', 'N^1.5', 'N2']:
        fn = comp_funcs[cfn]
        y0 = fn(range_n[0])
        cmp_time_rats = [fn(x)/y0 for x in range_n]
        
        time_ratios = [a/(b) for a, b, c in zip(rel_times, cmp_time_rats, range_n)]
        cmp_time_str = ', '.join(f"{x:.3f}" for x in time_ratios)
        avg_time_rat = sum(time_ratios[1:]) / (len(time_ratios)-1)
        if avg_time_rat>1.1:
            comp_res = 'Slower than'
        elif avg_time_rat < 0.9:
            comp_res = 'Faster than'
        else:
            comp_res = 'About the same as'
        print(f"{comp_res} ({avg_time_rat:.2f}x) for O({cfn}) function: [{cmp_time_str}]")
        


def sci_not(x:int, prec=8):
    if x != x//1:
        raise ValueError(f"Expected integer for scientific notation, got float: {x}")
    sx = get_digits(x)
    decimals = sx[1:prec]

    return f"{sx[0]}.{''.join(str(d) for d in decimals[1:])} E+{len(sx)-1}"


part_calc = em.PartitionsCalculator()
# print(part_calc.saved_partitions)
# print(part_calc.saved_pentagonals)
for z in range(0, 50):
    part_z = bench_ns(part_calc.partitions, 5, z)
    # print(part_calc.saved_partitions)
    
    print(f"p({z}) = {part_z}\n")

print(len(part_calc.saved_pentagonals), "pent numbers saved")