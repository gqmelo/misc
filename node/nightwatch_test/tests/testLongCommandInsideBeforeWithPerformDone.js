describe('Google demo test for Mocha', function() {

  describe('with Nightwatch', function() {

    before(function(client, done) {
      console.log('before');
      this.timeout(50000);
      client.pause(25000);
      client.perform(function (){
        done();
      });
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
      client.pause(25000);
      // Calling done here works fine
      done();
    });

    it('opens blank page', function(client) {
      client
        .url('about:blank')
        .assert.equal(true, true);
    });

  });
});
