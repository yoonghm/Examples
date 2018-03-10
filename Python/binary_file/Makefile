CC=gcc
CFLAGS=-I.

PROG=check_hole write_data read_data
#all: check_hole write_data read_data
all: $(PROG)

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

clean:
	rm -f $(PROG) database.db
