#!/usr/bin/env python3

import logging

# The default logging level s WARNING
logging.debug   ('This is for programmer'  ) # Will not be printed out
logging.info    ('This is for information' ) # Will not be printed out
logging.warning ('This is a warning!'      ) # Will     be printed out
logging.error   ('This is a software error') # Will     be printed out
logging.critical('This is a critical error') # Will     be printed out
