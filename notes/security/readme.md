# Security Notes

## Some Known Security Pitfalls

### Optimized Asserts

Python offers the ability to execute code in an optimized way. This allows the code to run faster and with less memory.

To run Python in optimized mode use `-O` or `-OO` it:

- removes `assert` statements
- sets the special builtin name `__debug__` to `False`
- removes docstrings from the code (with `-OO`)

If your logic uses `assert` and you run your code in the optimized mode, then this can be potential pitfall.

### `os.makedirs` Permissions

`os.makedirs("A/B/C", mode=0o700)`

In Python 3.7+, only the last folder `C` has permission 700 and the other folders `A` and `B` are created with the default permission 755.

### Absolute Path Joins

`os.path.join(path, *paths)`

If one of the appended components starts with a `/`, all previous components including the basepath are removed and this component is treated as an absolute path.

### Arbitrary Temp Files

`tempfile.NamedTemporaryFile(prefix=...)`

If an attacker passes the payload `/../var/www/test` as the `prefix` parameter, the following tmp file is created: `/var/www/test_abc123`

### Extended Zip Slip

Functions `TarFile.extractall()` and `TarFile.extract()` are known to be vulnerable to a *Zip Slip* attack. That's when an attacker tampers with the file names inside an archive so that they contain path traversal `(../)` characters.

### Incomplete Regex Match

Sometimes regex is used to detect malicious strings (however it is not recommended 
to use regex for deny lists). Sometimes regex can be bypassed.

### IP Address Normalisation

In Python < 3.8, IP addresses are normalized by the ipaddress library so that 
leading zeros are removed. This behavior might look harmless at first glance, 
but it has already led to a high-severity vulnerability.

An attacker can exploit the normalization to bypass potential validators for 
Server-Side Request Forgery (SSRF) attacks.
