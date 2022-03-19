# Pytest Notes

## Useful Options

`--collect-only` - shows you which tests will be run with the given options and 
configuration without actual test execution.

`-k EXPRESSION` - lets you use an expression to find what test functions to run. 
It can be used as a shortcut to running an individual test if its name is unique, 
or running a set of tests that have a common prefix or suffix in their names.
`and`, `or`, and `not` can be used to create complex expressions.

`-m MARKEXPR` - allows setting specific markers to filter tests out, tests should
be marked with `@pytest.mark.your_mark`. `and`, `or`, and `not` can be used to 
combine multiple markers.

`--durations=N` - reports the slowest N number of tests/setups/teardowns after 
the tests run. Use 0 for all tests.

`-r chars` - show extra test summary info as specified by given chars (see help).

`--setup-show` - show what fixtures are run.

`--cache-show` - show information about stored cache data. Data is stored in 
`.pytest_cache` directory.

`--markers` - show registered markers.

`--pdb` - get into standard interactive debugger pdb on test failures.

## Tests Project Layout (Best Practice)

- All of the tests are kept in `tests` folder and separate from the package source files in `src`.
- Functional and unit tests are separated into their own directories. Organizing test files into multiple 
directories allows you to easily run a subset of tests.
- The `__init__.py` files, that are in the tests folders, are empty. They tell **pytest** to
go up one directory to look for the root of the test directory and to look for the `pytest.ini` file.
- The `pytest.ini` file is optional. It contains project-wide pytest configuration. There
should be at most only one of these in your project. It can contain directives
that change the behavior of **pytest**, such as setting up a list of options that
will always be used.
- The `conftest.py` file is optional. It is considered by **pytest** as a "local plugin"
and can contain *hook functions* and *fixtures*. *Hook functions* are a way to
insert code into part of the **pytest** execution process to alter how pytest works.

## Marking Tests

**pytest** allows you to put markers on tests.

A test can have more than one marker, and a marker can be on multiple tests.

## Fixtures

*Fixtures* are functions that are run by **pytest** before (and sometimes after) the 
actual test functions. The code in the *fixture* can do whatever you want it to. 
You can use *fixtures* to get a data set for the tests to work on. You can use 
*fixtures* to get a system into a known state before running a test. *Fixtures* 
are also used to get data ready for multiple tests.

The `@pytest.fixture()` decorator is used to tell pytest that a function is a *fixture*.
When you include the *fixture* name in the parameter list of a test function,
**pytest** knows to run it before running the test. *Fixtures* can do work, and 
can also return data to the test function.

`autouse` indicates that all tests in this file will use the fixture and to run 
all of the time. As a good rule, opt for named fixtures (instead of `autouse`) 
unless you have a really great reason not to.

**pytest** allows you to rename *fixtures* with a `name` parameter to `@pytest.fixture()`.

You can also mark a test or a class with `@pytest.mark.usefixtures('fixt1', 'fixt2')`.
`usefixtures` takes a string that is composed of a comma-separated list of fixtures
to use.

*Fixtures* can be parameterized. With *parametrized fixtures*, every test 
function that uses that *fixture* will be called multiple times.

### Sharing Fixtures Through `conftest.py`

You can put *fixtures* into individual test files, but to share *fixtures* among 
multiple test files, you need to use a `conftest.py` file somewhere centrally 
located for all of the tests.

*Fixtures* can be shared by any test. You can put *fixtures* in individual test 
files if you want the *fixture* to only be used by tests in that file. Likewise, 
you can have other `conftest.py` files in subdirectories of the top tests directory.

Although `conftest.py` is a Python module, it **should not be imported** by test 
files. Don’t import `conftest` from anywhere. The `conftest.py` file gets read 
by **pytest**, and is considered a local plugin.

Any time you put *fixtures* and/or hook functions into a project’s top-level 
`conftest.py` file, you create a local conftest plugin.

### Fixture Scope

*Fixtures* include an optional parameter called `scope`, which controls how often
a *fixture* gets set up and torn down. The default `scope` is `function`.

The `scope` is set at the definition of a *fixture*, and not at the place where it’s called.

*Fixtures* can only depend on other *fixtures* of their same scope or wider.

- `scope='function'` - Run once per test function.
- `scope='class'` - Run once per test class, regardless of how many test methods are in the class.
- `scope='module'` - Run once per module, regardless of how many test functions or methods or other fixtures in the module use it.
- `scope='session'` - Run once per session.

### Builtin Fixtures

- `tmp_dir` - if you’re testing something that reads, writes, or modifies files, you can use
tmpdir to create files or directories used by a single test. It has function scope.
- `tmpdir_factory` - sets up a directory for many tests. It has session scope.
- `pytestconfig` - allows you to control how **pytest** runs through
command-line arguments and options, configuration files, plugins, and the
directory from which you launched **pytest**. The `pytestconfig` *fixture* is a shortcut
to `request.config`. You can also access builtin options with `pytestconfig`, 
not just options you add, as well as information about how **pytest** was 
started (the directory, the arguments, and so on).
- `cache` - allows storing information about one test session and retrieving it 
in the next.
- `capsys` - provides two bits of functionality: it allows you to retrieve 
stdout and stderr from some code, and it disables output capture temporarily.
- `monkeypatch` - Dynamic modification of a class or module during runtime. 
During testing, it is a convenient way to take over part of the runtime 
environment of the code under test and replace input/output dependencies with 
objects or functions that are more convenient for testing. The `monkeypatch` 
builtin *fixture* allows you to do this in the context of a single test. When 
the test ends the original unpatched is restored, undoing everything changed by 
the patch. See docs for examples.
- `recwarn` - allows you to examine warnings generated by code under test.

## Running Tests

To run specific test:

```
# Function
pytest test/test_suite.py::test_uno

# Entire Class Suite
pytest test/test_suite.py::TestSuite

# Specific Test in a Class Suite
pytest test/test_suite.py::TestSuite::test_dos
```

## Test Status

- PASSED (.): The test ran successfully.
- FAILED (F): The test did not run successfully (or XPASS + strict).
- SKIPPED (s): The test was skipped. `@pytest.mark.skip()` or `pytest.mark.skipif()` decorators.
- XFAIL (x): The test was not supposed to pass, ran, and failed. `@pytest.mark.xfail()` decorator.
- XPASS (X): The test was not supposed to pass, ran, and passed.
- ERROR (E): An exception happened outside of the test function, in either a fixture or in a hook function.

## Hooks

*Hook functions* - are another way to control how **pytest** behaves and are 
used frequently in plugins.

## Plugins

Plugins can include hook functions that alter **pytest**'s behavior.

For **pytest** plugin installation via `setuptools` we should specify 
`entry_points` dict with `'pytest11': ['plugin_name = plugin_path', ]`. 
`pytest11` is a special identifier that **pytest** looks for. With this line, 
we are telling **pytest** the name of our plugin and its path.

### Useful Plugin List

- `pytest-repeat` - To run tests more than once per session.
- `pytest-xdist` - Run tests in parallel
- `pytest-timeout` - Put time limits on your tests
- `pytest-instafail` - See details of failures and errors as they happen
- `pytest-sugar` - Instafail + Colors + Progress Bar
- `pytest-flake8` - Check for style plus linting
- `pytest-django` - Test Django applications
- `pytest-clarity` - A plugin to improve the output of pytest with colourful unified diffs
- `pytest-parallel` - A pytest plugin for parallel and concurrent testing
- `pytest-cov` - Coverage plugin for pytest

### Testing Plugins

Plugins are code that needs to be tested just like any other code. However,
testing a change to a testing tool is a little tricky. To solve that we use a 
plugin called `pytester` that ships with **pytest** but is disabled by default.

To enable `pytester` we add `pytest_plugins = 'pytester'` to the `conftest.py`.

## Code Coverage

We can get the summary from the command line with `pytest --cov=<module> <testsfolder>`

## Add Custom CLI Options Notes

Adding command-line options via `pytest_addoption` should be done via plugins
or in the `conftest.py` file at the top of your project directory structure. You
shouldn’t do it in a test subdirectory.

## Configuration

- `pytest.ini` - This is the primary **pytest** configuration file that allows 
you to change default behavior.
- `conftest.py` - This is a local plugin to allow hook functions and *fixtures* 
for the directory where the `conftest.py` file exists and all subdirectories.
- `__init__.py` - When put into every test subdirectory, this file allows you to
have identical test filenames in multiple test directories. If you have 
`__init__.py` files in all of your test subdirectories, you can have the same 
test filename show up in multiple directories.

If you set `addopts` in `pytest.ini` to the options you want, you don’t have to 
type them in anymore. For example:

```
[pytest]
addopts = -rsxX -l --tb=short --strict
```

### Registering Markers to Avoid Marker Typos

Example of registering markers in `pytest.ini`:

```
[pytest]
addopts = -rsxX -l --tb=short --strict
markers =
  foo: Run the foo tests
  bar: Run the bar tests
```

If markers aren’t registered, they won’t show up in the `--markers` list.

If you use `--strict`, any misspelled or unregistered markers show up as an error.

### Stopping pytest from Looking Directories

```
[pytest]
norecursedirs = .* venv src *.egg dist build
```

### Specifying Test Directories

```
[pytest]
testpaths = tests
```

## Changing Test Discovery Rules

**pytest** finds tests to run based on certain test discovery rules. The 
standard test discovery rules are:

- Start at one or more directory. You can specify filenames or directory
names on the command line. If you don’t specify anything, the current
directory is used.
- Look in the directory and all subdirectories recursively for test modules.
- A test module is a file with a name that looks like `test_*.py` or `*_test.py`.
- Look in test modules for functions that start with `test_`.
- Look for classes that start with `Test`. Look for methods in those classes
that start with `test_` but don’t have an `__init__` method.

#### python_classes

If we want to name test classes differently we can do that via:

```
[pytest]
python_classes = *Test Test* *Suite
```

#### python_files

If we want to name test files differently we can do that via:

```
[pytest]
python_files = test_* *_test check_*
```

#### python_functions

If we want to name test functions differently we can do that via:

```
[pytest]
python_functions = test_* check_*
```

## Internals

**pytest** includes a feature called *assert rewriting* that intercepts `assert` calls and
replaces them with something that can tell you more about why your assertions failed.

## Tools Integrations

#### tox

```
[pytest]
addopts = -rsxX -l --tb=short --strict
xfail_strict = true
...
```
