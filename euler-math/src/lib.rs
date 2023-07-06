use pyo3::{prelude::*, exceptions::PyTypeError, intern};
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
    Ok(())
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
fn divisors_of_n(n:usize) -> PyResult<Vec<usize>> {
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

    /*
    let mut is_div = vec![true;max_div];

    for div in 2..=max_div {
        if !is_div[div-1] {continue;}

        let rem = n % div;
        if rem > 0 {
            for mdiv in (div..=max_div).step_by(div) {
                is_div[mdiv-1] = false;
            }
        }
    }
    
    Ok(
        is_div.into_iter().enumerate()
            .filter_map(|(i,x)| if x {Some(i+1)} else {None})
            .collect::<Vec<usize>>()
    )
    */

}

#[pyfunction]
fn get_primes(max_n: u128) -> PyResult<Vec<u128>> {

    let mut nums = (0..=max_n).into_iter()
        .collect::<Vec<u128>>();

    for fctr in 2..=(max_n as usize) {
        if nums[fctr] > 0 {
            nums.iter_mut().step_by(fctr).skip(2)
                .for_each(|x| *x = 0);
        }
    }
    
    Ok(
        nums.into_iter()
            .filter(|&x| x > 1)
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

    fn incr_by(&mut self, times: usize) -> PyResult<i128> {
        let mut res=Err(PyErr::new::<PyTypeError,_>("Failed to get new Fib number."));
        for _i in 0..times {
            res = self.incr()
        }
        res
    }
}

