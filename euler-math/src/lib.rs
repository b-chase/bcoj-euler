use std::collections::hash_map::DefaultHasher;
use std::ops::{Div, Rem, Add, Sub, Mul};
use num_traits::{One, Zero, ToPrimitive, FromPrimitive, PrimInt};
use std::hash::{Hash, Hasher};
use pyo3::{prelude::*, exceptions::PyTypeError, pyclass::CompareOp};
use num_bigint::BigUint;
#[allow(unused)]
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
    m.add_function(wrap_pyfunction!(factorial, m)?)?;
    m.add_function(wrap_pyfunction!(factorial_split,m)?)?;
    m.add_function(wrap_pyfunction!(factorial_primes,m)?)?;
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
fn factorial(num: u128) -> PyResult<BigUint> {
    Ok((2_u128..=num).into_par_iter().map(|x| BigUint::from(x)).product())
}

#[pyfunction]
fn factorial_primes(num: u32) -> PyResult<BigUint> {
    if num <= 1 {
        return Ok(BigUint::from(1_u32));
    } else if num < 20 {
        return Ok(BigUint::from((1u32..=num).into_par_iter().product::<BigUint>()));
    }

    let mut res = if unum && 1 {BigUint::from(num)} else {BigUint::from(1)};
    unum >>= 1;
    let prime_list = _fast_primes(unum>>1);

    return Ok(prime_list.into_par_iter()
        .map(|p| {
            let p32 = p as u32;
            let mut p_pow = 0_u32;
            let mut max_div = p32;
            while max_div <= num {
                p_pow += num.div_euclid(max_div);
                max_div *= p32;
            }
            // println!("{}^{} = {}", p, p_pow, up.pow(p_pow));
            return BigUint::from(p32).pow(p_pow);
        }).product::<BigUint>()
    );
}

#[pyfunction]
fn factorial_split(num: u128) -> PyResult<BigUint> {
    if num <= 1 {
        return Ok(BigUint::from(1_u32));
    }

    // get the number of places, 'p', after the leading bit - 2^p < N
    let max_pow2 = u128::BITS - num.leading_zeros() - 1;
    let pow2_ct: u128 = (2_u32..=max_pow2)
        .into_par_iter()
        .map(|i| num >> i)
        .sum();
    
    let odd_terms = (2..=num).into_par_iter()
        .map(|x| BigUint::from(x >> x.trailing_zeros()))
        .product::<BigUint>();
    
    Ok(odd_terms << (pow2_ct as u32))

}

#[allow(unused)]
#[pyfunction]
fn factorial_prime_swing(num: u128) -> PyResult<u128> {
    // via P. Luschny -- https://oeis.org/A000142/a000142.pdf

    let prime_list = get_primes(num)?;

    fn prime_range(start: u128, stop: u128, primes: &Vec<u128>) -> Vec<u128> {
        primes.iter()
            .filter(|&&p| start <= p && p < stop)
            .cloned()
            .collect::<Vec<u128>>()
    }

    fn swing(m: u128, primes: &Vec<u128>) -> u128 {
        if m < 4 {return vec![1,1,1,3][m as usize];}

        let mut factors = prime_range(m.div_euclid(2)+1, m+1, &primes);

        let m_rt = int_sqrt(m).unwrap();

        for prime in prime_range(3, m_rt+1, &primes) {
            if prime >= m_rt+1 {
                break;
            }

            let mut p = 1;
            let mut q = m;

            loop {
                q /= prime;
                if q == 0 {break;}
                if q & 1 == 1 {
                    p *= prime;
                }
            }
            if p > 1 {
                factors.push(p)
            }
        }

        let mut add_factors = prime_range(m_rt+1, m.div_euclid(3)+1, &primes)
            .iter().filter(|&&x| (m.div_euclid(x)) & 1 == 1)
            .cloned().collect();
        factors.append(&mut add_factors);
        factors.iter().cloned().reduce(|acc,x| acc*x).unwrap()
    }

    fn odd_factorial(m: u128, primes: &Vec<u128>) -> u128 {
        if m < 2 {1}
        else {
            odd_factorial(m.div_euclid(2).pow(2), primes)*swing(m, primes)
        }
    }

    Ok(
        if num < 2 {1}
        else if num < 20 {
            (2..=num).into_iter().reduce(|acc,x| acc*x).unwrap()
        } else {
            let mut big_n = num;
            let mut bits = num;
            while big_n != 0 {
                bits -= big_n & 1;
                big_n >>= 1;
            }
            odd_factorial(num, &prime_list) * 2_u128.pow(bits as u32)
        }
    )
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
        let dos = T::from(2_u32).unwrap();
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

