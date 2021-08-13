# Binding Notes

## Rust

### PyO3

For more performance, make sure you do computationally heavy tasks with Rust's
native types. If you want to optimize your performance you should first of all
convert any Rust (Python-native) to Rust native types as soon as possible in
your code.

If your code is very simple, then usually native Python code will work faster
because of convert overhead.
