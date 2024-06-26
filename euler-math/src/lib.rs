use std::collections::{hash_map::DefaultHasher, HashSet};
#[allow(unused)]
use num_traits::{One, Zero, ToPrimitive, FromPrimitive, PrimInt};
use std::hash::{Hash, Hasher};
use pyo3::{prelude::*, exceptions::PyTypeError, pyclass::CompareOp};
use num_bigint::*;
use rayon::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
fn euler_math(_py: Python, m: &PyModule) -> PyResult<()> {
    // m.add_function(wrap_pyfunction!(Fibonacci, m)?)?;
    m.add_class::<Fibonacci>()?;
    m.add_function(wrap_pyfunction!(get_primes, m)?)?;
    m.add_function(wrap_pyfunction!(int_sqrt, m)?)?;
    m.add_function(wrap_pyfunction!(sum_to_n, m)?)?;
    m.add_function(wrap_pyfunction!(divisors_of_n, m)?)?;
    m.add_class::<Period>()?;
    m.add_function(wrap_pyfunction!(periodicity, m)?)?;
    m.add_function(wrap_pyfunction!(gcd, m)?)?;
    m.add_function(wrap_pyfunction!(prime_factors, m)?)?;
    m.add_function(wrap_pyfunction!(pell_numbers, m)?)?;
    m.add_function(wrap_pyfunction!(root_cont_fraction, m)?)?;
    m.add_class::<Fraction>()?;
    m.add_class::<RootContFraction>()?;
    m.add_function(wrap_pyfunction!(totient, m)?)?;
    // m.add_function(wrap_pyfunction!(pswing_factorial, m)?)?;
    m.add_function(wrap_pyfunction!(factorial_split,m)?)?;
    m.add_class::<PartitionsCalculator>()?;
    m.add_function(wrap_pyfunction!(long_divide,m)?)?;
    m.add_function(wrap_pyfunction!(pythagorean_triples,m)?)?;
    m.add_function(wrap_pyfunction!(product,m)?)?;
    Ok(())
}

pub trait UnsignedInteger {}
impl UnsignedInteger for usize {}
impl UnsignedInteger for u16 {}
impl UnsignedInteger for u32 {}
impl UnsignedInteger for u64 {}
impl UnsignedInteger for u128 {}
impl UnsignedInteger for BigUint {}


#[pyfunction]
fn product(terms: Vec<i128>) -> PyResult<i128> {
    Ok(terms.into_par_iter().product())
}


#[pyfunction]
fn pythagorean_triples(max_small_side: u128) -> PyResult<Vec<(u128,u128,u128)>> {
    
    let mut res_set: HashSet<(u128,u128,u128)> = HashSet::new();

    let mut m:u128 = 1;
    let mut loopvar = true;
    // loop over possible values and add primitives to result
    while loopvar {
        for n in 1..m {
            // do stuff here
            let mut a = m.pow(2) - n.pow(2);
            let mut b = 2 * m * n;
            let c = m.pow(2) + n.pow(2);

            (a,b) = (a.min(b), a.max(b));

            if a > max_small_side {
                if n == 1 {
                    loopvar = false;
                }
                break;
            }
            let mut d = 1;
            while a*d <= max_small_side {
                res_set.insert((a*d, b*d, c*d));
                d += 1;
            }
        }
        m += 1;
    }

    let res = res_set.into_iter().collect::<Vec<(u128,u128,u128)>>();
    Ok(res)
}


#[pyfunction]
fn long_divide(a:BigUint, b:BigUint, max_terms: Option<usize>) -> PyResult<Vec<BigUint>> {

    let mut res = vec![a.clone() / b.clone()];

    let mut remainder = BigUint::from(10_u32) * (a % b.clone());

    for _ in 0..max_terms.unwrap() {
        if remainder == BigUint::from(0_u32) {
            break
        }
        res.push(remainder.clone() / b.clone());
        remainder = BigUint::from(10_u32) * (remainder % b.clone());
    }

    Ok(res)
}


#[pyclass(get_all, set_all)]
struct PartitionsCalculator {
    saved_partitions: Vec<BigInt>, 
    saved_pentagonals: Vec<usize>
}

#[pymethods]
impl PartitionsCalculator {
    #[new]
    fn new() -> Self {
        let mut gen_pent = vec![0];
        // add first 20 terms to pentagonals for a start
        for n in 1..=5_usize {
            let pn_plus = (3*n*n - n).div_euclid(2);
            let pn_minus = (3*n*n + n).div_euclid(2);
            gen_pent.push(pn_plus);
            gen_pent.push(pn_minus);
        }
        PartitionsCalculator { saved_partitions: vec![BigInt::from(1), BigInt::from(1), BigInt::from(2)], saved_pentagonals: gen_pent }
    }

    fn partitions(&mut self, num: u128) -> PyResult<BigInt> {
        let usize_num = num as usize;
        if usize_num < self.saved_partitions.len() {
            return Ok(self.saved_partitions[usize_num].clone());
        }
        
        let mut i = self.saved_pentagonals.len().div_euclid(2);
        while usize_num >= 2*i {
            i += 1;
            let i2_by_3 = 3*i*i;  // not sure how much faster this will be, but might as well
            self.saved_pentagonals.push((i2_by_3 - i).div_euclid(2));
            self.saved_pentagonals.push((i2_by_3 + i).div_euclid(2));
        }
        
        let max_prev = self.saved_partitions.len();
        // ensure that all pengagonal numbers up to 
        for k in max_prev..usize_num {
            let _tmp = self.partitions(k as u128);
        }
        
        let total: BigInt  = (1..usize_num).into_par_iter()
            .filter_map(|n| {
                let pn = self.saved_pentagonals[n];
                if pn <= usize_num {
                    let index = usize_num - pn;
                    // Every two terms flip to positive or negative
                    let part = &self.saved_partitions[index] * (if ((n-1) & 2) < 2 {1} else {-1});
                    // println!("Adding P({}={}-{}) = {:?}", index, usize_num, pn, part);
                    Some(part)
                } else {
                    None
                }
            }).sum();
        
        self.saved_partitions.push(total.clone());

        Ok(total)

    }
}



// #[pyfunction]
// fn pswing_factorial(num: BigUint) -> PyResult<BigUint> {
//     Ok(num.factorial())
// }

#[pyfunction]
fn factorial_split(num: u128) -> PyResult<BigUint> {
    if num <= 1 {
        return Ok(BigUint::from(1_u32));
    }

    // get the number of places, 'p', after the leading bit - 2^p < N
    let m = num.div_euclid(2);
    let even_product = factorial_split(m)?;
    
    let odd_product = (1..=num).step_by(2).into_iter()
        .par_bridge()
        .map(|x| BigUint::from(x >> x.trailing_zeros()))
        .product::<BigUint>();
    
    Ok((odd_product * even_product) << m)

}


#[pyfunction]
fn totient(num: u128) -> PyResult<u128> {
    let mut result = num + 0;
    let mut n = num + 0;
    if n % 2 == 0 {
        while n % 2 == 0 {
            n >>= 1;
        }
        result -= result >> 1;
    }

    let mut p = 3;
    while p * p <= n {
        if n % p == 0 {
            while n % p == 0 {
                n = n / p;
            }
            result = result - result / p;
        }
        p += 2;
    }

    if n > 1 {
        result -= result / n;
    }

    Ok(result)
}



#[pyclass(get_all, set_all)]
struct Fraction {
    numerator: u32, 
    denominator: u32
}

#[pymethods]
impl Fraction {
    #[new]
    fn new(numer:u32, denom:u32) -> Fraction {
        Fraction { numerator: numer, denominator: denom }
    }

    fn reduce(&mut self) -> PyResult<()> {

        let div = _gcd(self.numerator, self.denominator) as u32;
        self.numerator /= div;
        self.denominator /= div;

        Ok(())
    }
    
    // fn __add__(&self, other: &PyInt) -> PyResult<Fraction> {
    //     let ri = u128::from(other.to_string());
    //     let other_frac = Fraction {numerator: other.extract::<u128>(), denominator: 1};
    //     Ok(self.__add__(other_frac));
    // }
    
    fn __hash__(&self) -> PyResult<u64> {
        let mut hasher = DefaultHasher::new();
        let tuple = (self.numerator, self.denominator);
        tuple.hash(&mut hasher);
        Ok(hasher.finish())
    }

    fn __repr__(&self) -> String {
        format!("{}/{}", self.numerator, self.denominator)
    }

    fn __eq__(&self, other: &Fraction) -> bool {
        if self.denominator == other.denominator {
            return self.numerator == other.denominator;
        } else {
            return self.numerator * other.denominator == other.numerator * self.denominator;
        }
    }

    fn __richcmp__(&self, other: &Self, op: CompareOp) -> PyResult<bool> {
        match op {
            CompareOp::Lt => Ok(self.__lt__(other)),
            CompareOp::Le => Ok(self.__le__(other)),
            CompareOp::Eq => Ok(self.__eq__(other)),
            CompareOp::Ne => Ok(!self.__eq__(other)),
            CompareOp::Gt => Ok(self.__gt__(other)),
            CompareOp::Ge => Ok(self.__ge__(other)),
        }
    }

    fn __lt__(&self, other: &Self) -> bool {
        if self.denominator == other.denominator {
            return self.numerator < other.denominator;
        } else {
            return self.numerator * other.denominator < other.numerator * self.denominator;
        }
    }

    fn __gt__(&self, other: &Self) -> bool {
        if self.denominator == other.denominator {
            return self.numerator > other.denominator;
        } else {
            return self.numerator * other.denominator > other.numerator * self.denominator;
        }
    }

    fn __le__(&self, other: &Self) -> bool {
        if self.denominator == other.denominator {
            return self.numerator <= other.denominator;
        } else {
            return self.numerator * other.denominator <= other.numerator * self.denominator;
        }
    }

    fn __ge__(&self, other: &Self) -> bool {
        if self.denominator == other.denominator {
            return self.numerator >= other.denominator;
        } else {
            return self.numerator * other.denominator  >= other.numerator * self.denominator;
        }
    }

    fn __add__(&self, other: &Self) -> PyResult<Fraction> {
        if self.denominator==other.denominator {
            return Ok(Fraction {
                numerator: self.numerator+other.numerator, 
                denominator: self.denominator
            })
        } else {
            let numer = self.numerator*other.denominator + other.numerator*self.denominator;
            let denom = self.denominator * other.denominator;
            let div = _gcd(numer, denom) as u32;
            return Ok(Fraction {
                numerator: numer/div, 
                denominator: denom/div
            })
        }
    }

    fn __sub__(&self, other: &Self) -> PyResult<Fraction> {
        if self.denominator==other.denominator {
            return Ok(Fraction {
                numerator: self.numerator-other.numerator, 
                denominator: self.denominator
            })
        } else {
            let numer = self.numerator*other.denominator - other.numerator*self.denominator;
            let denom = self.denominator * other.denominator;
            let div = _gcd(numer, denom) as u32;
            return Ok(Fraction {
                numerator: numer/div, 
                denominator: denom/div
            })
        }
    }

    fn __mul__(&self, other: &Self) -> PyResult<Fraction> {
    
        let numer = self.numerator*other.numerator;
        let denom = self.denominator * other.denominator;
        let div = _gcd(numer, denom) as u32;
        return Ok(Fraction {
            numerator: numer/div, 
            denominator: denom/div
        })
    }

    fn __truediv__(&self, other: &Self) -> PyResult<Fraction> {
        let numer = self.numerator*other.denominator;
        let denom = self.denominator * other.numerator;
        let div = _gcd(numer, denom) as u32;
        return Ok(Fraction {
            numerator: numer/div, 
            denominator: denom/div
        })
    }

}



#[pyclass(get_all)]
struct RootContFraction {
    num: u128, 
    terms: Vec<u128>, 
    _denom: u128, 
    _carryover: u128, 
    int_rt: u128
}

#[pymethods]
impl RootContFraction {
    #[new]
    fn new(whole_number: u128) -> Self {
        let int_rt = int_sqrt(whole_number).unwrap();
        let terms = vec![int_rt];
        let _carryover = int_rt;
        
        RootContFraction { 
            num: whole_number, 
            terms: terms, 
            _denom: 1, 
            _carryover: _carryover, 
            int_rt: int_rt 
        }
    }

    fn next(&mut self) -> u128 {
        let denom = self._denom;
        if denom == 0 {
            return 0;
        }
        
        let b = self._carryover;
        let new_numer = self.int_rt + b;
        let new_denom = (self.num - b.pow(2)) / denom;
        
        let next_term = new_numer.div_euclid(new_denom);
        
        self.terms.push(next_term);
        self._denom = new_denom;
        self._carryover = next_term * new_denom - b;
        
        next_term
    }

    
}

#[pyfunction]
fn root_cont_fraction(num: u128, max_terms: usize) -> PyResult<Vec<u128>> {

    let rt = int_sqrt(num)?;
    // a0 + rt(n) - a0 = a0 + (1 / 1 / (rt(n) - a0) ) 
    // 1/(rt(n)-a0) = (rt(n)+a0) / (n - a0^2) 
    
    let mut res = vec![rt];
    
    let mut denom = 1;
    let mut b = rt;
    for _i in 0..max_terms {
        let new_denom = num - b.pow(2);
        if new_denom == 0 {
            return Ok(res);
        }

        if new_denom < denom {
            println!("Error, new denominator {} is larger than previous {}", new_denom, denom);
            println!("Encountered computing fraction for sqrt({}) : {:?}", num, res);
            return Ok(res);
        }

        denom = new_denom / denom;
        let numer = rt + b;
        let new_term = numer.div_euclid(denom);
        b = new_term * denom - b;
        
        res.push(new_term);

    }

    Ok(res)
}


#[pyfunction]
fn pell_numbers(max_n: usize) -> PyResult<Vec<BigUint>> {

    let mut back_1: BigUint = BigUint::from(1_u32);
    let mut back_2: BigUint = BigUint::from(0_u32);
    let mut pell_nums = vec![back_1.clone(), back_2.clone()];
    let big_2 = BigUint::from(2_u32);
    for _n in 2..=max_n {
        let next_pell_num = &big_2*&back_1 + &back_2;
        back_2 = back_1;
        back_1 = next_pell_num.clone();
        pell_nums.push(next_pell_num.clone());
    }

    Ok(pell_nums)
}


#[pyfunction]
fn gcd(a: u128, b: u128) -> PyResult<u128> {
    Ok(_gcd(a, b))
}

fn _gcd<T: Into<u128> + std::ops::Rem + std::cmp::PartialEq>(a: T, b: T) -> u128 {
    let mut nb = b.into();
    let mut na = a.into();
    while nb != 0 {
        let remainder = na % nb;
        na = nb;
        nb = remainder;
    }
    na 
}

#[pyclass(get_all)]
struct Period {
    repetitions: usize,
    period_length: Option<usize>, 
    pattern: Option<Vec<i32>>
}

#[pyfunction]
fn periodicity(seq: Vec<i32>) -> PyResult<Period> {
    for pstart in 0..(seq.len()) {
        let sub_seq = &seq[pstart..(seq.len())];
    
        for plen in 1..=(sub_seq.len()/2) {
            let even_divide = sub_seq.len() % plen == 0;
            let chunks = sub_seq.chunks_exact(plen).collect::<Vec<&[i32]>>();
            let pattern = chunks[0];
            
            let mut all_match = chunks.iter()
                .fold(true, |acc, &chk| acc && chk.iter().zip(pattern.iter()).all(|(a,b)| a==b));

            if !even_divide {
                let rem_ct = sub_seq.len() % plen;
                all_match = all_match && sub_seq.ends_with(&pattern[0..rem_ct]);
            }

            if all_match {
                return Ok(Period {repetitions: sub_seq.len() / plen, period_length: Some(plen), pattern: Some(Vec::from(pattern))});
            }
        }
    }

    let no_match = Period {repetitions: 0, period_length: None, pattern: None};
    Ok(no_match)
}


#[pyfunction]
fn int_sqrt(num: u128) -> PyResult<u128> {
    Ok(_fast_int_rt(num))
}

fn _fast_int_rt<T>(num: T) -> T 
where
    T: PrimInt + One
{
    if num <= T::one() {
        return num;
    } else {
        let dos = T::from(2_u64).unwrap();
        let mut high = num / dos;
        let mut low = (high + num/high) / dos;

        while low < high {
            high = low;
            low = (high + num/high) / dos;
        }

        return high;
    }

}

#[pyfunction]
fn sum_to_n(n:u128) -> PyResult<u128> {
    Ok(n * (n+1) / 2)
}

#[pyfunction]
fn prime_factors(n: usize) -> PyResult<Vec<usize>> {
    if n <= 3 {
        return Ok(vec![n])
    }

    let mut divs = divisors_of_n(n)?;

    let res = divs.iter_mut().filter_map(|x| {
        let Ok(x_div) = divisors_of_n(*x) else {todo!()};
        if x_div.len()==2 {
            return Some(*x);
        } else {
            return None;
        }
    }).collect();

    Ok(res)
}

#[pyfunction]
fn divisors_of_n(n:usize) -> PyResult<Vec<usize>> {

    if n == 1 {
        return Ok(vec![1]);
    } else if n <= 3 {
        return Ok(vec![1, n])
    }

    let max_div = int_sqrt(n as u128).unwrap() as usize;
    
    let mut smalls = vec![1_usize];
    let mut bigs = vec![n];
    for div in 2..=max_div {
        if n % div == 0 {
            smalls.push(div);
            let big_div = n / div;
            if big_div > div {bigs.push(big_div);}
        }
    }
    bigs.reverse();
    smalls.append(&mut bigs);

    Ok(smalls)

}

#[pyfunction]
fn get_primes(max_prime: u128) -> PyResult<Vec<u128>> {
    Ok(_fast_primes(max_prime as usize).into_par_iter().map(|x| x as u128).collect())
}

fn _fast_primes(max_n: usize) -> Vec<usize> {
    let mut sieve = vec![true;1+(max_n)];

    let max_div = _fast_int_rt(max_n);

    for fctr in 2..=(max_div) {
        if sieve[fctr]  {
            sieve.iter_mut().step_by(fctr).skip(2)
                .for_each(|x| *x = false);
        }
    }
    
    sieve.into_iter().enumerate().skip(2)
        .filter_map(|(i, x)| if x {Some(i)} else {None})
        .collect::<Vec<usize>>()
    
}

#[pyclass(get_all)]
struct Fibonacci {
    n: usize, 
    num: i128,
    prev: i128
}

#[pymethods]
impl Fibonacci {
    #[new]
    fn new() -> Self {
        Fibonacci {n:1, num:1, prev:0}
    }

    fn incr(&mut self) -> PyResult<i128> {
        
        (self.n, self.num, self.prev) = (self.n+1, self.num+self.prev, self.num);
 
        Ok(self.num)
    }

    fn __repr__(& self) -> PyResult<String> {
        Ok(self.num.to_string())
    }

    fn __str__(& self) -> PyResult<String> {
        Ok(self.num.to_string())
    }

    fn incr_by(&mut self, times: usize) -> PyResult<i128> {
        let mut res=Err(PyErr::new::<PyTypeError,_>("Failed to get new Fib number."));
        for _i in 0..times {
            res = self.incr()
        }
        res
    }
}

