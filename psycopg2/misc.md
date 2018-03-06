# node-postgres

node-postgres is an non-blocking PostgreSQL client for node.j, with pure JavaScript and optional native libpq bindings

## Install nodejs

```sh
$ sudo apt install nodejs
```

## Create Examples Directory

```sh
$ mkdir ~/pg
$ cd ~/pg
$ npm install pg
```

### ```helloworld.js``` - Query PostgreSQL database version

```js
var pg = require('pg');
var client = new pg.Client();

client.connect(function (err) {
  if (err) {
    console.error('connect:' + err);
    throw err;
  }

  client.query('SELECT version()', function (err, result) {
    if (err) {
      console.error('query:' + err);
      throw err;
    }

    console.log(result.rows[0]);

    client.end(function (err) {
      if (err) {
        console.error('end:' + err);
        throw err;
      }
    });
  });
});
```

Running the program, assuming PostgreSQL database is running

```sh
$ nodejs helloworld.js

{ version: 'PostgreSQL 9.6.1 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609, 64-bit' }
```

### ```pool.js``` - Pool of client connections to PostgreSQL database

```js
var pg = require('pg');
var pool = new pg.Pool();

// Get a client from the pool
pool.connect(function (err, client, done) {
  if (err) {
    console.error('connect:' + err);
    throw err;
  }

  client.query('SELECT now()', function (err, result) {
    if (err) {
      console.error('query:' + err);
      throw err;
    }

    console.log(result.rows[0]);
  });

  client.release(); // release the client to pool
});

pool.end();
```

```sh
$ nodejs pool.js

{ now: Sat Jan 21 2017 00:43:45 GMT+0800 (SGT) }
```
