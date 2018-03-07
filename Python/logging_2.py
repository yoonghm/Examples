#!/usr/bin/env python3

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s', \
    )

logging.debug   ('Debug    message')
logging.info    ('Info     message')
logging.warning ('Warning  message')
logging.error   ('Error    message')
logging.critical('Critical message')
