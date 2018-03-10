/* check_hole.c */

#include <stdio.h>
#include <stddef.h>

#include "data_struct.h"

tData d;

int main()
{
  size_t st = sizeof(tData);
  size_t s1 = sizeof(d.id);
  size_t s2 = sizeof(d.name);
  size_t s3 = sizeof(d.salary);
  size_t o1 = offsetof(tData, id);
  size_t o2 = offsetof(tData, name);
  size_t o3 = offsetof(tData, salary);

  printf("sizeof(tData) = %zu\n\n", st);

  printf("'id'     %3zu ...%3zu\n", o1, o1+s1-1);
  if (o2 != o1+s1) {
    printf("holes       %3zu\n", o2-o1-s1);
  }
  printf("'name'   %3zu ...%3zu\n", o2, o2+s2-1);
  if (o3 != o2+s2) {
    printf("holes       %3zu\n", o3-o2-s2);
  }
  printf("'salary' %3zu ...%3zu\n", o3, o3+s3-1);
  if (o3 != o3+s3) {
    printf("holes       %3zu\n", st-o3-s3);
  }
  printf("\n");
 
  return 0;
}

