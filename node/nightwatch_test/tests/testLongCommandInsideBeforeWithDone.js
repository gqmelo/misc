describe('Google demo test for Mocha', function() {

  describe('with Nightwatch', function() {

    before(function(client, done) {
      console.log('before');
      // This command is executed only at the end, after all tests finished
      // It also opens two selenium sessions
      client.pause(22000);
      done();
    });

    after(function(client, done) {
      console.log('after');
      client.end(function() {
        done();
      });
    });

    afterEach(function(client, done) {
      console.log('afterEach');
      done();
    });

    beforeEach(function(client, done) {
      console.log('beforeEach');
      done();
    });

    it('opens blank page and fail', function(client) {
      client
        .url('about:blank')
        .assert.equal(true, true);
    });

  });
});
