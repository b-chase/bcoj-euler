source venv/scripts/activate &&
maturin build -m euler-math/Cargo.toml -f &&
pip install euler-math euler-math/