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
