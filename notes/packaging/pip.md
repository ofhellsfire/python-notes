# Pip

## Pip Constraints Files

It is good practice to fully specify the versions of the packages in the requirements 
file in order to achieve repeatable installation via: `pip install -r requirements.txt`

`requirements.txt` contains every pinned versions - direct and indirect dependencies. 
Sometimes it is hard to recognize original dependencies from indirect.

`constraints.txt` allows us not to specify exact versions in `requirements.txt`

To use constraints feature we invoke the `pip` as follows:

```
pip install --constraint constraints.txt -r requirements.txt
```

### Constraints.txt

Constraint files are requirement files which only control which version of a requirement 
is installed, not whether it is installed or not. The `constraint.txt` syntax is 
the same as in `requirements.txt` and we want to have packages to be fixed to 
specific version.

Use `pip freeze > constraints.txt` to create constraints file.
