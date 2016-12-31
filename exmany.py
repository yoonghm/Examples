# Issue: https://github.com/psycopg/psycopg2/issues/491#issuecomment-269828979
# executemany is slow in inserting many rows
# executemany2 is a new variance to improve the speed

import os
import time
import psycopg2
from psycopg2 import extensions as ext


def paginate(seq, page_size=100):
    page = []
    it = iter(seq)
    while 1:
        try:
            for i in xrange(page_size):
                page.append(it.next())
            yield page
            page = []
        except StopIteration:
            if page:
                yield page
            return


class ExManyCursor(ext.cursor):
    def executemany2(self, sql, argslist, page_size=100):
        for page in paginate(argslist, page_size=page_size):
            sqls = []
            for args in page:
                sqls.append(self.mogrify(sql, args))
            self.execute(";".join(sqls))


if __name__ == '__main__':
    NRECS = 10000

    cnn = psycopg2.connect(os.environ.get("TEST_DSN", ""))
    cur = cnn.cursor(cursor_factory=ExManyCursor)
    cur.execute("""
        create table testmany (id serial primary key, num integer, data text)
        """)
    t0 = time.time()
    cur.executemany("insert into testmany (num, data) values (%s, %s)",
        ((i, "x" * (i % 200)) for i in xrange(NRECS)))
    t1 = time.time()
    print "classic: %s sec" % (t1 - t0)

    cur.execute("select count(*) from testmany")
    assert cur.fetchone()[0] == NRECS

    cur.execute("""
        create table testmany2 (id serial primary key, num integer, data text)
        """)
    cur.executemany2("insert into testmany2 (num, data) values (%s, %s)",
        ((i, "x" * (i % 200)) for i in xrange(NRECS)))
    t2 = time.time()
    print "joined: %s sec" % (t2 - t1)

    cur.execute("select count(*) from testmany2")
    assert cur.fetchone()[0] == NRECS
