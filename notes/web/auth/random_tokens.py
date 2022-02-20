"""
Random tokens generation examples
"""

import secrets


if __name__ == '__main__':
    token1 = secrets.token_bytes()
    token2 = secrets.token_hex()
    token3 = secrets.token_urlsafe()
    print(f'{token1=}')
    print(f'{token2=}')
    print(f'{token3=}')