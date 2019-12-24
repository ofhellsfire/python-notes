# Demonstrates practical context manager example

import contextlib


class Transaction:

    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)
    try:
        yield tx
    except:
        tx.rollback()
        raise
    tx.commit()


class Connection:

    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        self.xid += 1
        print(f'starting transaction {self.xid}')
        result = self.xid
        return result

    def _commit_transaction(self, xid):
        print(f'committing transaction {self.xid}')

    def _rollback_transaction(self, xid):
        print(f'rolling back transaction {self.xid}')


if __name__ == "__main__":
    conn = Connection()
    try:
        with start_transaction(conn) as tx:
            x = 2
            y = x + 2
            print(f'transaction 1 = {x} {y}')
            raise ValueError()
    except ValueError:
        print('Ooops!')

    try:
        with start_transaction(conn) as tx:
            x = 2
            y = x + 2
            print(f'transaction 2 = {x} {y}')
    except ValueError:
        assert False
