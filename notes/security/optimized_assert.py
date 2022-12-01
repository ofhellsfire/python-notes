"""
Shows what can happen if use assers with optimized mode.

Try to run as usual: python filename
Also try to run in optimized mode: python -O filename
"""

class User:

    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


def superuser_action(user, cmd):
    assert user.is_admin, f'User "{user.name}" does not have admin privileges'
    print(f'Execute cmd as {user.name}: {cmd}')


if __name__ == '__main__':
    ordinary_user = User('Vlad', is_admin=False)
    admin_user = User('Masha', is_admin=True)
    cmd = 'cat /etc/passwd'
    superuser_action(ordinary_user, cmd=cmd)
    superuser_action(admin_user, cmd=cmd)
