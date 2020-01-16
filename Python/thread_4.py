import threading
import time
import logging
import random
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s|%(levelname)s|%(threadName)-9s|%(thread)d|%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)

def f():
    t = threading.currentThread()
    r = random.randint(1,10)
    logging.debug('sleeping %s', r)
    time.sleep(r)
    logging.debug('ending')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()

    for i in range(3):
        t = threading.Thread(target=f)
        t.start()

    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is not main_thread:
            logging.debug('joining %s', t.getName())
            t.join()
    logging.debug('Program exit')
