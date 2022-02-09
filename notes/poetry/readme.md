# Poetry Notes

## Poetry Install

**NOTE:** Try to avoid installing **poetry** via `pip`, because **poetry** will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install **poetry** is by using the official `install-poetry.py` script.

## Poetry `pyproject.toml`

If a table name in `pyproject.toml` is tool-specific, it must be prefixed with tool. By using such a subtable, you can add instructions for different tools in your project.

Example: `[tool.pytest.ini_options]`

Useful link: https://python-poetry.org/docs/pyproject/

## Virtual Environments

By default **poetry** creates the virtual environments in the `virtualenvs/` folder of **poetry**'s cache directory (`~/.cache/pypoetry` for Linux)

## Poetry Commands

`poetry new <name> | poetry new <name> --name <package name> | poetry new --src <name>` - creates initial project structure

`poetry init` - start an interactive session to create a `pyproject.toml` file (useful for existing projects)

`poetry env list` - shows available virtual environments

`poetry install` command

1. The install command read `pyproject.toml` or `poetry.lock` file and installs all listed dependencies
2. If there's a `poetry.lock` file: **poetry** uses the exact versions listed in `poetry.lock`
3. If there is no `poetry.lock` file: **poetry** will resolves all dependencies from the `pyproject.toml` file and downloads the latest version of their files

`poetry install --no-dev` - to not install development dependencies

`poetry install --dry-run` - displays the operations in the terminal without executing any of them

`poetry config --list` - find a location of the initialized environment

`poetry lock` - processes all dependencies in `pyproject.toml` file and locks them into the `poetry.lock` file. Also updates your existing dependencies if newer versions that fit your version constraints are available. If you don’t want to update any dependencies that are already in the `poetry.lock` file, then use `--no-update` option.

`poetry update` - will update all your packages and their dependencies within their version constraints

`poetry update <package>` - will update specific package in the dependencies

`poetry update --dry-run` - displays the operations in the terminal without executing any of them

``poetry add `cat requirements.txt` `` - add dependencies from existing requirements.txt

`poetry export --output requirements.txt` - export dependencies into requirements.txt

`poetry check` - validate `pyproject.toml`

## Dependencies

### Version Constraints

`^` - means that **poetry** can install any version that matches the leftmost non-zero digit of the version string

`~` - tilde requirements specify a minimal version with some ability to update. If you specify a major, minor, and patch version or only a major and minor version, only patch-level changes are allowed. If you only specify a major version, then minor- and patch-level changes are allowed.

`*` - wildcard requirements allow for the latest (dependency dependent) version where the wildcard is positioned.

`>=`, `>`, `<`, `!=` - inequality requirements allow manually specifying a version range or an exact version to depend on.

`==` - this will tell Poetry to install this version and this version only. If other dependencies require a different version, the solver will ultimately fail and abort any install or update procedures.

Multiple version requirements can also be separated with a comma, e.g. `>= 1.2, < 1.5`.

### Dependencies Sources

`git` - to depend on a library located in a **git** repository

`path` - to depend on a library located in a local directory or file (Example: `my-package = { path = "../my-package/", develop = false }`)

`url` - to depend on a library located on a remote archive

### Dependecies Restrictions

- You can specify that a dependency should be installed only for specific Python versions (`pathlib2 = { version = "^2.2", python = "~2.7 || ^3.2" }`)
- For more complex install conditions for your dependencies, **poetry** supports environment markers via the `markers` property (`pathlib2 = { version = "^2.2", markers = "python_version ~= '2.7' or sys_platform == 'win32'" }`)
