from contextlib import contextmanager
from time import time, sleep


class cm_timer_1:
    def __init__(self):
        self.begin_time = time()

    def __enter__(self):
        pass

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('time:', time() - self.begin_time)


@contextmanager
def cm_timer_2():
    begin_time=time()
    yield 1
    print('time:', time() - begin_time)


if __name__ == '__main__':

    with cm_timer_1():
        sleep(3.5)

    with cm_timer_2():
        sleep(2.5)