# https://projecteuler.net/problem=86
"""<p>A spider, S, sits in one corner of a cuboid room, measuring $6$ by $5$ by $3$, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is $10$ and the path is shown on the diagram.</p>
<div class="center">
<img src="resources/images/0086.png?1678992052" class="dark_img" alt=""><br></div>
<p>However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.</p>
<p>It can be shown that there are exactly $2060$ distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of $M$ by $M$ by $M$, for which the shortest route has integer length when $M = 100$. This is the least value of $M$ for which the number of solutions first exceeds two thousand; the number of solutions when $M = 99$ is $1975$.</p>
<p>Find the least value of $M$ such that the number of solutions first exceeds one million.</p>

"""
  
import euler_math as em
from math import sqrt


def solve(debug=False):
    # largest side of cuboid allowed
    res = None  
    print("Getting triples")
    max_m = 100
    triples = em.pythagorean_triples(max_m*2)
    assert isinstance(triples, list)
    print(f"Found {len(triples)} triples with largest side less than {max_m}")
    
    triples.sort(key=lambda x: x[0] - 1/x[1])
    ways = set()
    for trip in triples:
        new_ways = set()
        a = trip[0]
        b = trip[1]
        for i in range(1,a):
            [x, y, z] = sorted([b, a-i, i])
            if z <= max_m:
                new_ways.add((x, y, z))
        for i in range(1,b):
            [x, y, z] = sorted([a, b-i, i])
            if z <= max_m:
                new_ways.add((x, y, z))
        ways = ways.union(new_ways)
        print(trip, len(ways))
    
    res = 0
    last = 0
    for way in sorted(ways, key=lambda x: x[2]):
        res += 1
        if way[2] > last:
            print(f"\n M <= {way[2]} ==> up to {res} ways", end="", flush=True)
            last = way[2]
        else:
            print(f"\r M <= {way[2]} ==> up to {res} ways", end="", flush=True)
            
    print()
    
    print(f'*** Answer: {res} ***')