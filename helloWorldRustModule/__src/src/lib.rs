use pyo3::prelude::*;

#[pymodule]
fn __lib(_py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "hello")]
    fn hello(_py: Python, msg: &str) -> PyResult<u32> {
        println!("Hello, {}!", msg);
        Ok(42)
    }

    Ok(())
}
