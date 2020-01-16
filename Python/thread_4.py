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
    r = random.randint(8,10)
    logging.debug('sleeping %s', r)
    time.sleep(r)
    logging.debug('ending')
    return

if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=f)
        t.name=f'Daemon Thread {str(i)}'
        t.setDaemon(True)
        t.start()

    for i in range(2):
        t = threading.Thread(target=f)
        t.name=f'Thread {str(i)}'
        t.start()

    logging.debug(f'Total active thread = {threading.active_count()}')
    time.sleep(5)
    logging.debug(f'Total active thread = {threading.active_count()}')

    main_thread = threading.main_thread()
    for t in threading.enumerate():
        logging.debug(t.name)
        if t is not main_thread:
            logging.debug('joining %s', t.getName())
            t.join()
    logging.debug('Program exit')
