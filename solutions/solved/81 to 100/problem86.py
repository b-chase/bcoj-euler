# https://projecteuler.net/problem=86
"""<p>A spider, S, sits in one corner of a cuboid room, measuring $6$ by $5$ by $3$, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is $10$ and the path is shown on the diagram.</p>
<div class="center">
<img src="resources/images/0086.png?1678992052" class="dark_img" alt=""><br></div>
<p>However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.</p>
<p>It can be shown that there are exactly $2060$ distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of $M$ by $M$ by $M$, for which the shortest route has integer length when $M = 100$. This is the least value of $M$ for which the number of solutions first exceeds two thousand; the number of solutions when $M = 99$ is $1975$.</p>
<p>Find the least value of $M$ such that the number of solutions first exceeds one million.</p>

"""
  
import euler_math as em
from euler_tools.math import generate_pythagorean_triples
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def cuboid_shortest_routes(p_triple: tuple[int,int,int], max_side_len:int) -> set[int]:
    shortest_route_dims = set()
    
    if p_triple[0]>max_side_len or p_triple[1] > 2*max_side_len:
        return shortest_route_dims
    
    assert p_triple[2]**2 == p_triple[1]**2 + p_triple[0]**2, f"Must supply pythagorean triple, got {p_triple[0]}^2 + {p_triple[1]}^2 != {p_triple[2]}^2"
    
    for a, b in [(p_triple[0], p_triple[1]), (p_triple[1], p_triple[0])]:
        route_dist_sq = a**2 + b**2
        dim1 = a
        for dim2 in range(max(1, b-max_side_len), b//2 + 1):
            dim3 = b - dim2
            assert dim3 >= dim2 and dim3 <= max_side_len, f"Dimension exceeds limit: {[dim1, dim2, dim3]}, from triple {p_triple}"
            dims = tuple(sorted([dim1, dim2, dim3]))
            if dims[2] > max_side_len:
                continue
            
            alt_dist_sq = min(dim2**2 + (dim1+dim3)**2, dim3**2 + (dim1+dim2)**2)
            if route_dist_sq <= alt_dist_sq:
                shortest_route_dims.add(dims)
    return shortest_route_dims

def solve(debug=False):
    # largest side of cuboid allowed
    res = None  
    print("Getting triples")
    max_m = 2000
    triples = em.pythagorean_triples(2*max_m)
    assert isinstance(triples, list)
    print(f"Found {len(triples)} triples with largest side less than {2*max_m}")
    
    triples.sort(key=lambda x: x[0] - 1/x[1])
    
    # other_triples = list(generate_pythagorean_triples(max_m))
    # other_triples.sort(key=lambda x: x[0] - 1/x[1])
    
    # for trip1, trip2 in zip(triples, other_triples):
    #     print(trip1, trip2)
    #     for trip in [trip1, trip2]:
    #         assert trip[0]**2 + trip[1]**2 == trip[2]**2
    #     assert trip1 == trip2, "Mismatched triples!"
    # return
    
    ways = set()
    
    with ThreadPoolExecutor() as executor:
        futures = []
        
        for trip in triples:
            futures.append(executor.submit(cuboid_shortest_routes, trip, max_m))
        
        for future in tqdm(as_completed(futures), desc="Checking triples...", total=len(futures)):
            new_ways = future.result()
            ways.update(new_ways)
    
    ct = 0
    last = 0
    target = 1000000
    
    for way in sorted(ways, key=lambda x: tuple(reversed(x))):
        ct += 1
        if res is None and ct >= target:
            res = way[2]
        if way[2] > last:
            print(f"\n M <= {way[2]} --> up to {ct} ways", end="", flush=True)
            last = way[2]
        else:
            print(f"\r M <= {way[2]} ==> up to {ct} ways", end="", flush=True)
            pass
            
    print()
    
    print(f'*** Answer: {res} ***')