# Structural Pattern Matching

Introduced in 3.10.

## Branch Reachability

Order of branches we specify matters. We can get the case where some branches 
cannot be reached because higher branch matches ealier. In this case consider 
putting such a branch close to the top.

## Exhaustiveness

Due to Python nature it is hard to catch the case when not all possible cases are 
covered by branches. In this case consider using static type checkers.

## Advanced Features

### RegEx Matching

Pattern matching does not provide matching patterns for regex out-of-the-box, but 
we can implement it easily by using `__eq__`.

See example: *regex_match.py*

### JSON Processing

Pattern matching is efficient for matching JSON structures in form of Python's dicts. 
This can be done via *mapping pattern* which is triggeted by `case {...}: ...`

See example: *json_match.py*

### Set Membership

We can use `__eq__` to match against sets of values.

See example: *set_membership.py*

### Matching Builtin Types

We can use structural pattern matching for matching builtin types.

See example: *builtin_types.py*

### Matching Positional Arguments

By default when using the *class pattern* to match a class like `case MyClass(key="value"): ...` 
we have to use keyword arguments. This can be a bit verbose. To ease we can 
use `__match_args__`.

See example: *positional_args.py*
