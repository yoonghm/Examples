/* write_data.c */

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

#include "data_struct.h"

tData db[] = {
        {4, "Tze Kong", 3200.0}
};

int main()
{
  int      fd;     /* File number                                     */
  size_t   ReSz;   /* Size of a tData record                          */
  size_t   n;      /* Number of records in db                         */

  /******************/
  /* Open data file */
  /******************/
  fd = open("./database.db", O_RDWR, 0644);
  if (fd<0) {
    perror("open(): ");
    return(-1);
  }

  /*************************/
  /* Go to the end of file */
  /*************************/
  lseek(fd, 0, SEEK_END);

  /************************/
  /* Write data into file */
  /************************/
  ReSz = sizeof(tData);
  n = sizeof(db)/ReSz;

  for (int i=0; i<n; i++) {
    ssize_t ret = write(fd, (const char *) &db[i], ReSz);
    if (ret != ReSz) {
      perror("write(): ");
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
