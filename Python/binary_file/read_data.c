/* read_data.c */

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

#include "data_struct.h"

int main()
{
  int      fd;     /* File number                                     */
  size_t   ReSz;   /* Size of a tData record                          */

  /******************/
  /* Open data file */
  /******************/
  fd = open("./database.db", O_RDONLY, 0644);
  if (fd<0) {
    perror("open(): ");
    close(fd);
    return(-1);
  }

  ReSz = sizeof(tData);

  /************************************/
  /* Read data file and print records */
  /************************************/
  tData r;         /* To store a record read from data file*/
  while (1) {
    ssize_t ret = read(fd, (char *) &r, ReSz);
    if (ret == ReSz) {
      printf("%ld\t%.*s\t$%.2f\n", r.id, (int) ReSz, r.name, r.salary);
    }
    else if (ret == 0)
      break;
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
