# node-postgres

node-postgres is an non-blocking PostgreSQL client for node.j, with pure JavaScript and optional native libpq bindings

## Installation

```sh
sudp apt install npm
$ npm install pg
```

### ```helloworld.js``` - Query PostgreSQL database version

```js
var pg = require('pg');
var client = new pg.Client(); // Use default environment variables

client.connect(function (err) {
  if (err) {
    console.error('Error connect to PostgreSQL');
  }
  // execute a query on our database
  client.query('SELECT version()', function (err, result) {
    if (err) {
      console.error('query error');
    }
    console.log(result.rows[0]);
  });
});
```

Running the program, assuming PostgreSQL database is running

```sh
nodejs
```

### ```pool.js``` - Pool of client connections to PostgreSQL database

```js
var pg = require('pg');
var pool = new pg.Pool(); // Use default environment variables

// Get a client and do something
pool.connect(function(err, client, done) {
  if (err) {
    console.error('Error connect to PostgreSQL via pool');
  }
  client.query('SELECT version()', function(err, result) {
    done(); // release the client to pool
    if (err) {
      console.error('query error');
    }
    console.log(result.rows[0]);
  });
});
```
