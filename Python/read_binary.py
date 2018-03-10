#!/usr/bin/env python3

######################################################################
# data_struct.h
######################################################################

'''C
/* data_struct.h */

typedef struct tData {
  long   id;       /* 8 bytes */
  char   name[8];  /* 8 bytes */
  float  salary;   /* 4 bytes */
} tData;
'''

######################################################################
# check_hole.c
######################################################################
'''C
/* check_hole.c */

#include <stdio.h>
#include <stddef.h>

#include "data_struct.h"

tData d;

int main()
{
  size_t s_tData  = sizeof(tData);
  size_t s_id     = sizeof(d.id);
  size_t s_name   = sizeof(d.name);
  size_t s_salary = sizeof(d.salary);

  printf("sizeof(tData) = %zu\n\n", sizeof(d));

  printf("'id'     is at = %3zu  occupies %zu bytes\n",
         offsetof(tData, id), s_id);
  printf("'name'   is at = %3zu  occupies %zu bytes\n",
         offsetof(tData, name), s_name);
  printf("'salary' is at = %3zu  occupies %zu bytes\n",
         offsetof(tData, salary), s_salary);

  printf("\n");

  if (s_tData != s_id + s_name + s_salary)
    printf("There is/are holes in tData.\n\n");

  return 0;
}
'''

######################################################################
# fill_data.c
######################################################################

'''
/* fill_data.c */

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

#include "data_struct.h"

tData db[] = {
        {1, "Hong Hua", 2000.0},
        {2, "Ali Mohd", 2000.0},
        {3, "Ravi Abu", 2200.0}
};

int main()
{
  int      fd;     /* File number                                     */
  size_t   ReSz;   /* Size of a tData record                          */
  size_t   n;      /* Number of records in db                         */

  /*****************************/
  /* Create and open data file */
  /*****************************/
  fd = open("./database.db", O_RDWR|O_CREAT|O_TRUNC, 0644);
  if (fd<0) {
    perror("open(): ");
    close(fd);
    return(-1);
  }

  /************************/
  /* Write data into file */
  /************************/
  ReSz = sizeof(tData);
  n = sizeof(db)/ReSz;

  for (int i = 0; i < n; i++) {
    ssize_t ret = write(fd, (const char *) &db[i], ReSz);
    if (ret == -1) {
      perror("write(): ");
      close(fd);
      return(-1);
    }
  }

  /************************************/
  /* Read data file and print records */
  /************************************/
  lseek(fd, SEEK_SET, 0); /* Move offset  to beginning of file */
  tData r;         /* To store a record read from data file*/
  for (int i = 0; i < n; i++) {
    ssize_t ret = read(fd, (char *) &r, ReSz);
    if (ret == ReSz) {
      printf("%ld\t%.*s\t$%.2f\n", r.id, (int) ReSz, r.name, r.salary);
    }
    else {
      perror("read(): ");
      close(fd);
      return(-1);
    }
  }

  /******************/
  /* Close the file */
  /******************/
  close(fd);

  return 0;
}
'''

from struct import Struct

x = Struct('q8sfxxxx')

with open('database.db', 'rb') as file:
  while True:
    buf = file.read(x.size)
    if len(buf) == x.size:
      print(x.unpack_from(buf))
    else:
      break
