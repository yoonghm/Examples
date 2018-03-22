#!/usr/bin/env python3

import lmdb
import shutil

db = 'dialcode'


def showAll():
    """Read everything from lmdb file"""
    cursor = lmdb.open(db, readonly=True).begin().cursor()
    for key, value in cursor:
        print(key.decode(), '=>', value.decode())
    print('')

# Create memory-mapped file lmdb file with default settings
env = lmdb.open(db)
with env.begin(write=True) as txn:  # Access lmdb file using transaction
    txn.put('Ipoh'.            encode(),   '605'.encode())
    txn.put('Malaysia'.        encode(),    '60'.encode())
    txn.put('Singapore'.       encode(),   '065'.encode())
print('All records in the database')
showAll()

# Delete Ipoh, which is a city, from the database
with env.begin(write=True) as txn:
    txn.delete('Ipoh'.encode())
print('Delete "Ipoh" from the databsae')
showAll()

# Add Germany with dial code 49 into the database
with env.begin(write=True) as txn:
    txn.put('Germany'.         encode(),    '49'.encode())
print('Add Germany into the database')
showAll()

# Replace dial code for Singapore to 65
with env.begin(write=True) as txn:
    txn.replace('Singapore'.   encode(),    '65'.encode())
print('Replace dial code for Singapore')
showAll()

# Close the environment
env.close()

# Delete lmdb folder
shutil.rmtree(db, ignore_errors=True)

