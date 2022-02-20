"""
Signed tokens generation/validation examples
"""

import jwt


if __name__ == "__main__":
    SECRET_KEY = "my_secret"
    ALGORITHM = "HS256"

    # token generation
    token1 = jwt.encode({"user_id": "user_uno", "user_role": "user"}, SECRET_KEY, algorithm=ALGORITHM)
    print(f'{token1=}')

    token2 = jwt.encode({"user_id": "user_dos", "user_role": "admin"}, SECRET_KEY, algorithm=ALGORITHM, headers={"version": "0.1.2"})
    print(f'{token2=}')

    invalid_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U'

    # token validation
    res = jwt.decode(token1, SECRET_KEY, algorithms=[ALGORITHM])
    print(f"{res=}")

    res = jwt.decode(token2, SECRET_KEY, algorithms=[ALGORITHM])
    print(f"{res=}")

    res = jwt.decode(invalid_token, SECRET_KEY, algorithms=[ALGORITHM])  # this must fail
    print(f"{res=}")
