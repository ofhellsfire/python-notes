"""
Note: only for 3.10+
"""

import re
from dataclasses import dataclass


@dataclass
class RegexEqual(str):
    string: str
    match: re.Match = None

    def __eq__(self, pattern):
        self.match = re.search(pattern, self.string)
        return self.match is not None
    
    def __getitem__(self, group):
        return self.match[group]


if __name__ == '__main__':
    print(bool(RegexEqual("Just some string") == r'^J.*ing$'))  # True

    # Simple RegEx Example
    match RegexEqual("Just some string to match"):
        case r"^...match":
            print("Noooo...")
        case r"^J.*ing$":
            print("Closer")
        case r"^J.*match$":
            print("Bingo!")

    # Capture Group RegEx Example
    match RegexEqual("His car is 'Chevrolet Blazer'"):
        case r"^His.+'(.+)'$" as capture:
            print(f"Captured: '{capture[1]}'")
        case _:
            print("Nothing is matched")
