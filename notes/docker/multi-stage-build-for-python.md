# Multi-Stage Builds For Python

In multi-stage builds, you build two different images:

- In the first image, you install the compiler and other build tools, and then 
compile your source code.
- In the second image, you install only the packages you need to run your code, 
and you copy in the compiled artifacts created by the first image.

In the general case, figuring out all the files you need to copy from the compiler 
stage to the runtime stage can be difficult. So there are several solutions:

## 1. Solution #1: `pip install --user`

If you install a package with pip’s `--user` option, all its files will be 
installed in the `.local` directory of the current user’s home directory. 
That means all the files will end up in a single place you can easily copy.

The main downside to this approach is that you are still sharing your Python 
install with any system Python packages that might exist in one of your 
system-level dependencies.

## Solution #2: virtualenv

A virtualenv is another way to get a single isolated directory you can copy over 
into your final Docker image.

