exports.command = function() {
  const client = this;
  console.log('goToGoogleAndSearch command');
  client
    .url('http://google.com')
    .expect.element('body').to.be.present.before(5000);

  client.setValue('input[type=text]', ['nightwatch', client.Keys.ENTER])
    .waitForElementPresent('#main')
    .assert.containsText('#main', 'Night Watch');
};
