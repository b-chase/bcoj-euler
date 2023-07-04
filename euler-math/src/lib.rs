use pyo3::{prelude::*, exceptions::PyTypeError};
use rayon;


#[pyfunction]
fn int_sqrt(num: u128) -> PyResult<u128> {
    if num <= 0 {
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
            .filter(|&x| x > 0)
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

// #[pyfunction]
// fn Fibonacci(n: i128) -> PyResult<i128> {
//     0
// }

/// A Python module implemented in Rust.
#[pymodule]
fn euler_math(_py: Python, m: &PyModule) -> PyResult<()> {
    // m.add_function(wrap_pyfunction!(Fibonacci, m)?)?;
    m.add_class::<Fibonacci>()?;
    m.add_function(wrap_pyfunction!(get_primes, m)?)?;
    m.add_function(wrap_pyfunction!(int_sqrt, m)?)?;
    Ok(())
}