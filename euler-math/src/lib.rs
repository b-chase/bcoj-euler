use pyo3::{prelude::*, exceptions::PyTypeError};
#[allow(unused)]
use rayon;

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

    m.add("__all__", vec!["Fibonacci", "get_primes", "int_sqrt", "sum_to_n", "divisors_of_n", "periodicity", "gcd", "prime_factors"])?;
    
    Ok(())
}

// #[pyfunction]
// fn continued_fraction()

#[pyfunction]
fn gcd(mut a: u32, mut b: u32) -> PyResult<u32> {
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }
    Ok(a)
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
    if num <= 1 {
        return Ok(num);
    } else {
        let mut high = num / 2;
        let mut low = (high + num/high) / 2;

        while low < high {
            high = low;
            low = (high + num/high) / 2;
        }

        return Ok(high);
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
            // let mut x_pow = 1;
            // while n % x.pow(x_pow) == 0 {
            //     x_pow += 1;
            // }
            // return Some(x.pow(x_pow-1));
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
fn get_primes(max_n: u128) -> PyResult<Vec<u128>> {
    let mut is_prime = vec![true;1+(max_n as usize)];

    let max_div = int_sqrt(max_n)?+1;

    for fctr in 2..=(max_div as usize) {
        if is_prime[fctr]  {
            is_prime.iter_mut().step_by(fctr).skip(2)
                .for_each(|x| *x = false);
        }
    }
    
    Ok(
        is_prime.into_iter().enumerate().skip(2)
            .filter_map(|(i, x)| if x {Some(i as u128)} else {None})
            .collect::<Vec<u128>>()
    )
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

