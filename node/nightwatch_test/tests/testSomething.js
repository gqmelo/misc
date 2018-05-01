describe('Google demo test for Mocha', function() {

  describe('with Nightwatch', function() {

    before(function(client, done) {
      console.log('before');
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

    it('opens google page and search without custom commands', function(client) {
      client
        .url('http://google.com')
        .expect.element('body').to.be.present.before(5000);

      /* On 0.9.21, when running with --verbose, we can see the message:
       * "We have failures in "opens google page and search without custom commands". Taking screenshot..."
       * but the test still pass.
       * On 1.0.4 it throws errors (Error while running .setElementValue() protocol action: undefined)
      **/
      client.setValue('input[type=text]', ['nightwatch', client.Keys.ENTER])
        .waitForElementPresent('#main')
        .assert.containsText('#main', 'Night Watch');
    });

    it('opens google page', function(client) {
      console.log('Calling goToGoogle command');
      // On 0.9.21 it seems to run fine (no error showed by --verbose)
      // On 1.0.4 the test hangs
      client.goToGoogle();
      console.log('Called goToGoogle command');
    });

    it('opens google page and search', function(client) {
      console.log('Calling goToGoogleAndSearch command');
      // Same results as the test without custom commands
      client.goToGoogleAndSearch();
      console.log('Called goToGoogleAndSearch command');
    });

    it('opens google page and search with inner command', function(client) {
      console.log('Calling goToGoogleAndSearchWithInnerCommand command');
      // Same results as the test without custom commands
      client.goToGoogleAndSearchWithInnerCommand();
      console.log('Called goToGoogleAndSearchWithInnerCommand command');
    });
  });
});
