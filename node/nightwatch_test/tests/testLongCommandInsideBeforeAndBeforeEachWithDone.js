describe('Google demo test for Mocha', function() {

  describe('with Nightwatch', function() {

    before(function(client, done) {
      console.log('before');
      // Now this executes, but in parallel with the pause from beforeEach
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
      // Executes in parallel with the pause from before.
      // So the total pause is only 25s instead of 47s
      client.pause(25000);
      done();
    });

    it('opens blank page and fail', function(client) {
      client
        .url('about:blank')
        .assert.equal(true, true);
    });

  });
});
