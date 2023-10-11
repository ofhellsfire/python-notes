from multiprocessing import Lock, Process
from multiprocessing.managers import BaseManager
from time import sleep


class Spreadsheet():

    def __init__(self):
        self.sheet = {
            'A1': None,
            'B1': None,
            'C1': None,
        }
        self._lock = Lock()

    def get_values(self):
        with self._lock:
            return self.sheet

    def get_value(self, cell):
        with self._lock:
            sleep(0)  # allow context switch
            return self.sheet.get(cell)
    
    def set_value(self, cell, value):
        with self._lock:
            try:
                sleep(0)
                self.sheet[cell] = value
            except KeyError:
                print(f'Invalid cell: {cell}')
                raise
    
    def append_value(self, cell, value):
            try:
                sleep(0)
                curr = self.get_value(cell)
                with self._lock:
                    if curr is None:
                        sleep(0)
                        curr = ''
                    sleep(0)
                    self.sheet[cell] = f"{curr}{value}"
            except KeyError:
                print(f'Invalid cell: {cell}')
                raise
    

class SpresheetManager(BaseManager):
    """Custom manager to support cutom classes"""


def emulate_user_one_actions(spreadsheet):
    # actions
    values = spreadsheet.get_values()
    spreadsheet.set_value('A1', 'Uno - ::1::')
    spreadsheet.append_value('C1', 'Tres')


def emulate_user_two_actions(spreadsheet):
    # actions
    values = spreadsheet.get_values()
    spreadsheet.set_value('B1', 'Dos - ::2::')
    spreadsheet.append_value('C1', ' - ::3::')


if __name__ == '__main__':
    SpresheetManager.register('Spreadsheet', Spreadsheet)
    with SpresheetManager() as manager:
        sheet = manager.Spreadsheet()
        user_one_process = Process(target=emulate_user_one_actions, args=(sheet,))
        user_two_process = Process(target=emulate_user_two_actions, args=(sheet,))
        user_one_process.start()
        user_two_process.start()
        user_one_process.join()
        user_two_process.join()
        print(f'Value: {sheet.get_values()}')
