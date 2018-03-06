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
