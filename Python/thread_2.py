#!/usr/bin/env python3

import threading
import time

# num is positional args, sleep is keyword argument
def worker(num, sleep=2):
  print('Worker: ', num)
  time.sleep(sleep)
  return

threads = []
for i in range(5):
  t = threading.Thread(target=worker,
                       args=(i,),
                       kwargs={'sleep':5}
                      )
  threads.append(t)
  t.start()

print('Waiting for child thread to return...')
