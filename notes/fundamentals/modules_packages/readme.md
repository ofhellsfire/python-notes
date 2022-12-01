# Modules & Packages

## Tips

### Non-empty `__init__.py` cases

1. We might add imports to `__init__.py` when we want to refactor code that has 
   grown into multiple modules without introducing breaking changes to existing 
   users. This also may provide a simplified API so users don't have to dig into 
   implementation details.
2. We might add logger initialization in the main package's `__init__.py` for use 
   across multiple modules.
3. We might add compatibility checks performing.

